# ADP Proof Infrastructure

**Version:** 2.1
**Status:** Reference Implementation Available
**Reference:** [Pressonify.ai](https://pressonify.ai)

---

## Overview

Proof Infrastructure is a v2.1 addition to ADP that addresses a critical gap: **verifying that AI systems actually use your ADP endpoints**.

Building ADP infrastructure is straightforward. Proving AI engagement is hard. Proof Infrastructure provides the tooling to close this gap.

---

## Components

### 1. Crawler Hit Tracking

Log every AI crawler request to ADP endpoints.

**Identified Crawlers (11):**

| Crawler | Organization | User Agent Pattern |
|---------|--------------|-------------------|
| GPTBot | OpenAI | `gptbot` |
| ClaudeBot | Anthropic | `claudebot` |
| PerplexityBot | Perplexity AI | `perplexitybot` |
| Google-Extended | Google | `google-extended` |
| Bingbot | Microsoft | `bingbot` |
| Cohere-AI | Cohere | `cohere-ai` |
| YouBot | You.com | `youbot` |
| Applebot-Extended | Apple | `applebot-extended` |
| Meta-ExternalAgent | Meta | `meta-externalagent` |
| CCBot | Common Crawl | `ccbot` |
| Diffbot | Diffbot | `diffbot` |

**Implementation Pattern:**

```python
import asyncio
from fastapi import Request

AI_CRAWLERS = {
    "GPTBot": "gptbot",
    "ClaudeBot": "claudebot",
    "PerplexityBot": "perplexitybot",
    "Google-Extended": "google-extended",
    "Bingbot": "bingbot",
    "Cohere-AI": "cohere-ai",
    "YouBot": "youbot",
    "Applebot-Extended": "applebot-extended",
    "Meta-ExternalAgent": "meta-externalagent",
    "CCBot": "ccbot",
    "Diffbot": "diffbot"
}

def identify_crawler(user_agent: str) -> str:
    """Identify AI crawler from user agent string."""
    if not user_agent:
        return "unknown"

    ua_lower = user_agent.lower()

    for crawler_name, pattern in AI_CRAWLERS.items():
        if pattern in ua_lower:
            return crawler_name

    if any(bot in ua_lower for bot in ["bot", "crawler", "spider"]):
        return "other_bot"

    return "human"

async def log_adp_hit(request: Request, endpoint: str):
    """Fire-and-forget logging - never blocks response."""
    asyncio.create_task(_log_adp_hit_async(request, endpoint))

async def _log_adp_hit_async(request: Request, endpoint: str):
    """Background task that logs the hit."""
    try:
        user_agent = request.headers.get("user-agent", "")
        crawler_name = identify_crawler(user_agent)
        ip_address = request.client.host

        # Insert into database
        await db.insert("adp_crawler_hits", {
            "endpoint": endpoint,
            "crawler_name": crawler_name,
            "user_agent": user_agent[:500],
            "ip_address": ip_address,
            "hit_at": datetime.utcnow().isoformat()
        })
    except Exception as e:
        # Never raise - background work shouldn't crash
        logger.warning(f"Failed to log ADP hit: {e}")
```

**Key Design Decisions:**

1. **Fire-and-forget** — Logging uses `asyncio.create_task()` so it never blocks the response
2. **Truncation** — User agents truncated to 500 chars to prevent DB bloat
3. **Silent failures** — Logging errors are caught and logged, never raised
4. **IP anonymization** — Consider hashing or truncating IPs for privacy

---

### 2. Citation Monitoring

Track when AI platforms cite content from your ADP-enabled site.

**Supported Platforms:**

| Platform | Method | Status |
|----------|--------|--------|
| Perplexity | API (`sonar` model) | Active |
| ChatGPT | Passive detection | Planned |
| Claude | Passive detection | Planned |
| Gemini | Passive detection | Planned |

**Query Templates:**

```python
QUERY_TEMPLATES = [
    "{company_name} press release",
    "{company_name} latest news",
    "{company_name} announcement",
    "{company_name} {industry} news",
    "{company_name} launch",
    "news about {company_name}"
]
```

**Perplexity API Integration:**

```python
import httpx
import hashlib

async def scan_perplexity_citations(company_name: str, target_domain: str) -> list:
    """Scan Perplexity for citations of your content."""
    citations = []

    for template in QUERY_TEMPLATES:
        query = template.format(company_name=company_name)
        query_hash = hashlib.sha256(query.encode()).hexdigest()

        # Check deduplication (skip if scanned in last 24h)
        if await is_recently_scanned(query_hash):
            continue

        response = await httpx.post(
            "https://api.perplexity.ai/chat/completions",
            headers={"Authorization": f"Bearer {PERPLEXITY_API_KEY}"},
            json={
                "model": "sonar",
                "messages": [{"role": "user", "content": query}],
                "return_citations": True
            }
        )

        data = response.json()

        # Extract citations pointing to target domain
        for citation in data.get("citations", []):
            if target_domain in citation.get("url", ""):
                citations.append({
                    "query": query,
                    "query_hash": query_hash,
                    "url": citation["url"],
                    "context": citation.get("text", "")[:500],
                    "platform": "perplexity"
                })

    return citations
```

**Deduplication:**

- SHA-256 hash of query text
- 24-hour window for deduplication
- Prevents redundant API calls

---

### 3. Public Transparency API

Expose aggregated crawler statistics via public endpoints.

**Endpoints:**

| Endpoint | Description |
|----------|-------------|
| `GET /api/v1/adp/stats` | Overall statistics (period, totals, breakdowns) |
| `GET /api/v1/adp/stats/crawlers` | Top crawlers ranked by hit count |
| `GET /api/v1/adp/stats/endpoints` | Top endpoints ranked by hit count |
| `GET /api/v1/adp/stats/daily` | Daily hit trends (time series) |
| `GET /api/v1/adp/stats/endpoint/{path}` | Specific endpoint deep-dive |

**Response Example:**

```json
{
  "period_days": 30,
  "start_date": "2025-11-27T00:00:00Z",
  "end_date": "2025-12-27T23:59:59Z",
  "total_hits": 2847,
  "ai_crawler_hits": 2156,
  "human_hits": 691,
  "crawler_breakdown": {
    "GPTBot": 892,
    "ClaudeBot": 567,
    "PerplexityBot": 423,
    "Google-Extended": 274
  },
  "endpoint_breakdown": {
    "/llms.txt": 1247,
    "/ai-discovery.json": 856,
    "/knowledge-graph.json": 432
  },
  "generated_at": "2025-12-27T20:00:00Z"
}
```

**Privacy Considerations:**

- Never expose individual IP addresses
- Aggregate data only
- Consider geographic breakdown at country level max

---

## Database Schema

```sql
-- Crawler hit logging
CREATE TABLE adp_crawler_hits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    endpoint VARCHAR(100) NOT NULL,
    crawler_name VARCHAR(100),
    user_agent TEXT,
    ip_address VARCHAR(45),
    referer TEXT,
    hit_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for efficient querying
CREATE INDEX idx_adp_hits_endpoint ON adp_crawler_hits(endpoint);
CREATE INDEX idx_adp_hits_crawler ON adp_crawler_hits(crawler_name);
CREATE INDEX idx_adp_hits_time ON adp_crawler_hits(hit_at DESC);
CREATE INDEX idx_adp_hits_endpoint_time ON adp_crawler_hits(endpoint, hit_at DESC);

-- Daily aggregation for dashboard performance
CREATE TABLE adp_crawler_stats_daily (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    date DATE NOT NULL,
    endpoint VARCHAR(100) NOT NULL,
    crawler_name VARCHAR(100) NOT NULL,
    hit_count INTEGER DEFAULT 0,
    UNIQUE(date, endpoint, crawler_name)
);

-- Citation tracking
CREATE TABLE adp_citations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content_id TEXT NOT NULL,
    platform TEXT NOT NULL,
    query_text TEXT NOT NULL,
    query_hash TEXT NOT NULL,
    cited_url TEXT NOT NULL,
    citation_context TEXT,
    verified BOOLEAN DEFAULT FALSE,
    found_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_citations_content ON adp_citations(content_id);
CREATE INDEX idx_citations_platform ON adp_citations(platform);
CREATE INDEX idx_citations_hash ON adp_citations(query_hash);
```

---

## Rate Limiting

Protect citation scanning endpoints from abuse:

```python
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)

@router.post("/scan/{content_id}")
@limiter.limit("5 per hour")
async def trigger_citation_scan(content_id: str):
    """Rate limited: 5 scans per hour per IP."""
    ...
```

---

## Reference Implementation

**Pressonify.ai** provides a complete reference implementation:

- **Crawler Stats:** https://pressonify.ai/api/v1/adp/stats
- **Citation Stats:** https://pressonify.ai/api/v1/citations/stats
- **Source Code:** Contact for licensing

**Live Endpoints:**

```bash
# Overall stats
curl https://pressonify.ai/api/v1/adp/stats?days=30

# Top crawlers
curl https://pressonify.ai/api/v1/adp/stats/crawlers

# Top endpoints
curl https://pressonify.ai/api/v1/adp/stats/endpoints

# Daily trends
curl https://pressonify.ai/api/v1/adp/stats/daily?days=14
```

---

## Implementation Checklist

- [ ] Add crawler identification to ADP endpoint handlers
- [ ] Implement fire-and-forget hit logging
- [ ] Create database tables for crawler hits
- [ ] Build aggregation queries for statistics
- [ ] Expose public transparency API endpoints
- [ ] (Optional) Integrate Perplexity API for citation monitoring
- [ ] (Optional) Add rate limiting for scan endpoints
- [ ] (Optional) Build dashboard visualization

---

## Why Proof Infrastructure Matters

1. **Credibility** — "We're AI-optimized" is a claim. "GPTBot hit us 892 times this month" is proof.

2. **Iteration** — If ClaudeBot isn't crawling `/knowledge-graph.json`, you know to investigate.

3. **Transparency** — Users can verify that AI systems engage with their content.

4. **Ecosystem trust** — Public transparency APIs help the industry understand AI crawler behavior.

---

*Proof Infrastructure is part of ADP v2.1, released December 27, 2025.*
*Specification: [github.com/BuddySpuds/AI-Discovery-Protocol](https://github.com/BuddySpuds/AI-Discovery-Protocol)*
