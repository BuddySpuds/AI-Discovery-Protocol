# Proof Infrastructure Documentation

**ADP v2.1 Feature**

Proof Infrastructure enables you to measure the effectiveness of your ADP implementation by tracking AI crawler visits, detecting citations, and attributing ROI to specific content.

---

## Overview

Implementing ADP is only valuable if you can prove it works. Proof Infrastructure provides three capabilities:

1. **Crawler Hit Logging** - Track when AI systems visit your ADP endpoints
2. **Citation Detection** - Monitor when AI systems cite your content
3. **ROI Attribution** - Connect citations back to source content

---

## 1. Crawler Hit Logging

### Tracked AI Crawlers

| Crawler | Organization | User-Agent Pattern |
|---------|--------------|-------------------|
| GPTBot | OpenAI | `GPTBot/1.0` |
| ChatGPT-User | OpenAI | `ChatGPT-User` |
| ClaudeBot | Anthropic | `ClaudeBot` |
| Claude-Web | Anthropic | `Claude-Web` |
| PerplexityBot | Perplexity | `PerplexityBot` |
| Google-Extended | Google | `Google-Extended` |
| Amazonbot | Amazon | `Amazonbot` |
| Bytespider | ByteDance | `Bytespider` |
| cohere-ai | Cohere | `cohere-ai` |
| Meta-ExternalAgent | Meta | `Meta-ExternalAgent` |
| anthropic-ai | Anthropic | `anthropic-ai` |

### Implementation (Python/FastAPI)

```python
from fastapi import Request
from datetime import datetime
import asyncio

# Crawler identification patterns
AI_CRAWLERS = [
    ("GPTBot", "openai"),
    ("ChatGPT-User", "openai"),
    ("ClaudeBot", "anthropic"),
    ("Claude-Web", "anthropic"),
    ("PerplexityBot", "perplexity"),
    ("Google-Extended", "google"),
    ("Amazonbot", "amazon"),
    ("Bytespider", "bytedance"),
    ("cohere-ai", "cohere"),
    ("Meta-ExternalAgent", "meta"),
    ("anthropic-ai", "anthropic"),
]

async def log_adp_crawler_hit(request: Request, endpoint: str):
    """Fire-and-forget crawler hit logging"""
    user_agent = request.headers.get("User-Agent", "")

    for crawler_name, organization in AI_CRAWLERS:
        if crawler_name.lower() in user_agent.lower():
            # Log to database (async, non-blocking)
            asyncio.create_task(
                save_crawler_hit({
                    "crawler": crawler_name,
                    "organization": organization,
                    "endpoint": endpoint,
                    "user_agent": user_agent,
                    "ip_address": request.client.host,
                    "timestamp": datetime.utcnow().isoformat(),
                })
            )
            return crawler_name

    return None

# Middleware for automatic logging
@app.middleware("http")
async def adp_crawler_middleware(request: Request, call_next):
    # Only log ADP endpoints
    adp_endpoints = [
        "/ai-discovery.json",
        "/knowledge-graph.json",
        "/llms.txt",
        "/llms-full.txt",
        "/feed.json",
        "/news/",
    ]

    if any(request.url.path.startswith(ep) for ep in adp_endpoints):
        await log_adp_crawler_hit(request, request.url.path)

    return await call_next(request)
```

### Database Schema

```sql
CREATE TABLE adp_crawler_hits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    crawler VARCHAR(50) NOT NULL,
    organization VARCHAR(50),
    endpoint VARCHAR(255) NOT NULL,
    user_agent TEXT,
    ip_address VARCHAR(45),
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_crawler_hits_timestamp ON adp_crawler_hits(timestamp);
CREATE INDEX idx_crawler_hits_crawler ON adp_crawler_hits(crawler);
CREATE INDEX idx_crawler_hits_endpoint ON adp_crawler_hits(endpoint);
```

### Analytics Queries

```sql
-- Crawler hits by day
SELECT
    DATE(timestamp) as date,
    crawler,
    COUNT(*) as hits
FROM adp_crawler_hits
WHERE timestamp > NOW() - INTERVAL '30 days'
GROUP BY DATE(timestamp), crawler
ORDER BY date DESC, hits DESC;

-- Most crawled endpoints
SELECT
    endpoint,
    COUNT(*) as total_hits,
    COUNT(DISTINCT crawler) as unique_crawlers
FROM adp_crawler_hits
WHERE timestamp > NOW() - INTERVAL '7 days'
GROUP BY endpoint
ORDER BY total_hits DESC;

-- Crawler activity trend
SELECT
    DATE_TRUNC('week', timestamp) as week,
    COUNT(*) as hits
FROM adp_crawler_hits
GROUP BY week
ORDER BY week DESC
LIMIT 12;
```

---

## 2. Citation Detection

### Detection Methods

#### Method 1: Perplexity API (Recommended)

Use the Perplexity Sonar API to search for citations:

```python
import httpx
from typing import List, Dict

PERPLEXITY_API_KEY = "your-api-key"

async def scan_for_citations(
    company_name: str,
    keywords: List[str]
) -> Dict:
    """Scan Perplexity for citations of your content"""

    # Wide-net query templates (optimized for detection)
    query_templates = [
        # Tier 1: Direct queries (86% success rate)
        {"template": f"tell me about {company_name}", "category": "direct", "priority": 1},
        {"template": f"what is {company_name}", "category": "direct", "priority": 1},
        {"template": company_name, "category": "direct", "priority": 1},

        # Tier 2: News queries (40% success rate)
        {"template": f"{company_name} announcement", "category": "news", "priority": 2},
        {"template": f"{company_name} latest news", "category": "news", "priority": 2},

        # Tier 3: Generic queries (29% success rate)
        {"template": f"{company_name} press release", "category": "generic", "priority": 3},
        {"template": f"recent news about {company_name}", "category": "generic", "priority": 3},
    ]

    citations = []

    async with httpx.AsyncClient() as client:
        for query_info in sorted(query_templates, key=lambda x: x["priority"]):
            response = await client.post(
                "https://api.perplexity.ai/chat/completions",
                headers={
                    "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "sonar",
                    "messages": [
                        {"role": "user", "content": query_info["template"]}
                    ],
                    "return_citations": True
                }
            )

            if response.status_code == 200:
                data = response.json()
                if "citations" in data:
                    for citation in data["citations"]:
                        if your_domain in citation.get("url", ""):
                            citations.append({
                                "url": citation["url"],
                                "query": query_info["template"],
                                "category": query_info["category"],
                                "platform": "perplexity",
                                "discovered_at": datetime.utcnow().isoformat()
                            })

    return {
        "total_citations": len(citations),
        "citations": citations,
        "queries_run": len(query_templates)
    }
```

#### Method 2: Manual Verification

For platforms without APIs, use manual spot checks:

```python
VERIFICATION_PROMPTS = [
    "What are the best press release platforms?",
    "Tell me about [Your Company]",
    "What's the latest news from [Your Company]?",
    "[Your Company] reviews"
]

# Test these prompts on:
# - ChatGPT (chat.openai.com)
# - Claude (claude.ai)
# - Perplexity (perplexity.ai)
# - Gemini (gemini.google.com)
```

### Citation Database Schema

```sql
CREATE TABLE ai_citations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    platform VARCHAR(50) NOT NULL,  -- 'perplexity', 'chatgpt', 'claude', 'gemini'
    query TEXT NOT NULL,
    query_category VARCHAR(50),
    cited_url TEXT NOT NULL,
    citation_text TEXT,
    discovered_at TIMESTAMPTZ DEFAULT NOW(),
    attributed_pr_id UUID REFERENCES press_releases(id),
    confidence_score DECIMAL(3,2),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_citations_platform ON ai_citations(platform);
CREATE INDEX idx_citations_discovered ON ai_citations(discovered_at);
CREATE INDEX idx_citations_attributed ON ai_citations(attributed_pr_id);
```

---

## 3. ROI Attribution

### Attribution Algorithm

Connect discovered citations back to source content:

```python
from difflib import SequenceMatcher

async def attribute_citation_to_pr(citation: Dict, press_releases: List[Dict]) -> Dict:
    """Match a citation to its source press release"""

    best_match = None
    best_score = 0.0

    for pr in press_releases:
        score = 0.0

        # Method 1: URL matching (highest confidence)
        if citation["cited_url"] == pr["url"]:
            return {
                "pr_id": pr["id"],
                "confidence": 1.0,
                "method": "url_exact"
            }

        # Method 2: URL contains PR slug
        if pr["slug"] in citation["cited_url"]:
            score = 0.9

        # Method 3: Headline similarity
        headline_similarity = SequenceMatcher(
            None,
            citation.get("citation_text", "").lower(),
            pr["headline"].lower()
        ).ratio()

        if headline_similarity > 0.7:
            score = max(score, headline_similarity * 0.85)

        # Method 4: Company name matching
        if pr["company_name"].lower() in citation.get("query", "").lower():
            score = max(score, 0.6)

        if score > best_score:
            best_score = score
            best_match = pr

    if best_match and best_score >= 0.6:
        return {
            "pr_id": best_match["id"],
            "confidence": best_score,
            "method": "fuzzy_match"
        }

    return None
```

### Metrics Dashboard

```python
async def get_citation_metrics(days: int = 30) -> Dict:
    """Calculate citation ROI metrics"""

    # Total citations in period
    total_citations = await db.fetchval("""
        SELECT COUNT(*) FROM ai_citations
        WHERE discovered_at > NOW() - INTERVAL '$1 days'
    """, days)

    # Citations by platform
    by_platform = await db.fetch("""
        SELECT platform, COUNT(*) as count
        FROM ai_citations
        WHERE discovered_at > NOW() - INTERVAL '$1 days'
        GROUP BY platform
        ORDER BY count DESC
    """, days)

    # Published PRs in period
    total_prs = await db.fetchval("""
        SELECT COUNT(*) FROM press_releases
        WHERE published_at > NOW() - INTERVAL '$1 days'
    """, days)

    # Citation rate
    citation_rate = total_citations / max(total_prs, 1)

    # Average time to citation
    avg_time_to_citation = await db.fetchval("""
        SELECT AVG(EXTRACT(EPOCH FROM (c.discovered_at - p.published_at)) / 86400)
        FROM ai_citations c
        JOIN press_releases p ON c.attributed_pr_id = p.id
        WHERE c.discovered_at > NOW() - INTERVAL '$1 days'
    """, days)

    return {
        "period_days": days,
        "total_citations": total_citations,
        "total_prs_published": total_prs,
        "citation_rate": round(citation_rate, 2),
        "avg_time_to_citation_days": round(avg_time_to_citation or 0, 1),
        "by_platform": dict(by_platform),
        "generated_at": datetime.utcnow().isoformat()
    }
```

---

## 4. Public Stats API

Expose your ADP stats publicly to demonstrate effectiveness:

### `/api/v1/adp/stats` Endpoint

```python
@app.get("/api/v1/adp/stats")
async def get_adp_stats():
    """Public ADP statistics endpoint"""

    # Crawler stats (last 30 days)
    crawler_stats = await db.fetch("""
        SELECT crawler, COUNT(*) as hits
        FROM adp_crawler_hits
        WHERE timestamp > NOW() - INTERVAL '30 days'
        GROUP BY crawler
        ORDER BY hits DESC
    """)

    # Citation stats
    citation_stats = await get_citation_metrics(30)

    return {
        "version": "2.1",
        "period": "30_days",
        "crawler_hits": {
            "total": sum(r["hits"] for r in crawler_stats),
            "by_crawler": {r["crawler"]: r["hits"] for r in crawler_stats}
        },
        "citations": citation_stats,
        "endpoints_served": 17,
        "generated_at": datetime.utcnow().isoformat()
    }
```

**Example Response:**

```json
{
  "version": "2.1",
  "period": "30_days",
  "crawler_hits": {
    "total": 1247,
    "by_crawler": {
      "GPTBot": 523,
      "ClaudeBot": 312,
      "PerplexityBot": 198,
      "Google-Extended": 145,
      "Amazonbot": 69
    }
  },
  "citations": {
    "total_citations": 36,
    "total_prs_published": 12,
    "citation_rate": 3.0,
    "avg_time_to_citation_days": 2.4,
    "by_platform": {
      "perplexity": 24,
      "chatgpt": 8,
      "claude": 4
    }
  },
  "endpoints_served": 17,
  "generated_at": "2026-01-08T12:00:00Z"
}
```

---

## 5. Daily Reports

### Email Report Template

```python
async def send_daily_citation_report():
    """Send daily citation report at 8pm GMT"""

    metrics = await get_citation_metrics(7)

    # Get detailed per-PR breakdown
    pr_citations = await db.fetch("""
        SELECT
            p.headline,
            p.company_name,
            p.published_at,
            COUNT(c.id) as citation_count,
            ARRAY_AGG(DISTINCT c.platform) as platforms
        FROM press_releases p
        LEFT JOIN ai_citations c ON c.attributed_pr_id = p.id
        WHERE p.published_at > NOW() - INTERVAL '7 days'
        GROUP BY p.id
        ORDER BY citation_count DESC
    """)

    html_content = f"""
    <h1>Daily Citation Report</h1>
    <p>Period: Last 7 days</p>

    <h2>Summary</h2>
    <ul>
        <li>Total Citations: {metrics['total_citations']}</li>
        <li>Citation Rate: {metrics['citation_rate']} per PR</li>
        <li>Avg Time to Citation: {metrics['avg_time_to_citation_days']} days</li>
    </ul>

    <h2>By Platform</h2>
    <ul>
        {''.join(f"<li>{p}: {c}</li>" for p, c in metrics['by_platform'].items())}
    </ul>

    <h2>Per-PR Breakdown</h2>
    <table>
        <tr><th>Headline</th><th>Company</th><th>Citations</th><th>Platforms</th></tr>
        {''.join(f"<tr><td>{pr['headline']}</td><td>{pr['company_name']}</td><td>{pr['citation_count']}</td><td>{', '.join(pr['platforms'] or [])}</td></tr>" for pr in pr_citations)}
    </table>
    """

    await send_email(
        to="admin@example.com",
        subject=f"Citation Report: {metrics['total_citations']} citations this week",
        html=html_content
    )
```

### GitHub Actions Cron Job

```yaml
# .github/workflows/daily-citation-report.yml
name: Daily Citation Report

on:
  schedule:
    - cron: '0 20 * * *'  # 8pm GMT daily
  workflow_dispatch:  # Manual trigger

jobs:
  send-report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install httpx

      - name: Run citation report
        env:
          PERPLEXITY_API_KEY: ${{ secrets.PERPLEXITY_API_KEY }}
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
          RESEND_API_KEY: ${{ secrets.RESEND_API_KEY }}
        run: python scripts/daily_citation_report.py
```

---

## 6. Cost Optimization

### Perplexity API Costs

| Volume | Monthly Cost |
|--------|-------------|
| 4 PRs/week | ~$5.50/month |
| 10 PRs/week | ~$14/month |
| 25 PRs/week | ~$35/month |

**Cost Breakdown:**
- Perplexity Sonar: $5/1K requests
- ~8 queries per PR scan
- Minimal token costs

### Optimization Strategies

1. **Batch scanning** - Scan all recent PRs once daily, not on publish
2. **Query prioritization** - Run high-success queries first, stop early if found
3. **Caching** - Cache negative results for 24 hours
4. **Sampling** - For high-volume sites, sample 20% of content

---

## Reference Implementation

Live proof infrastructure at Pressonify.ai:
- Stats API: https://pressonify.ai/api/v1/adp/stats
- Crawler logs: Internal dashboard
- Citation tracking: Perplexity API integration

---

*AI Discovery Protocol v2.1 - Proof Infrastructure*
*Maintained by [Pressonify](https://pressonify.ai)*
