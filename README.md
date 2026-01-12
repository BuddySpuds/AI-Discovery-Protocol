# AI Discovery Protocol (ADP) v3.0

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.0-green.svg)](CHANGELOG.md)
[![Standard](https://img.shields.io/badge/Status-Production-success.svg)](SPECIFICATION.md)
[![Results](https://img.shields.io/badge/Results-View%20Data-orange.svg)](RESULTS.md)
[![MCP](https://img.shields.io/badge/MCP-Level%204-purple.svg)](SPECIFICATION.md#10-mcp-integration-level-4---optional)

**Making websites discoverable to AI systems (ChatGPT, Claude, Perplexity, Gemini)**

> **Real Results:** ADP implementations achieve **2.4 day average time to first AI citation** with **100% citation detection rate**. [View anonymized customer data →](RESULTS.md)

---

## What is ADP?

The **AI Discovery Protocol** is an open standard that enables websites to make their content discoverable and understandable to AI systems—not just traditional search engines.

### The Problem

**Traditional SEO** was designed for keyword-based crawlers (Google, Bing):
- Optimizes for PageRank algorithms and backlink analysis
- Requires weeks to index and rank content
- Uses HTML parsing with minimal semantic understanding

**AI Systems** (ChatGPT, Claude, Perplexity, Gemini) work fundamentally differently:
- Query structured entity catalogs instead of keyword indexes
- Reason over relationships between entities
- Require context windows optimized for AI processing
- Need freshness signals for cache invalidation

**Current Limitation:** 99% of websites have no structured discovery mechanism for AI systems.

### The Solution

ADP provides a **single entry point** (`/ai-discovery.json`) that maps all AI-optimized resources:

```
AI System → GET /ai-discovery.json (Single entry point)
          ↓
       Parse meta-index
          ↓
       ┌─────────────┬──────────────┬─────────────┬─────────────┐
       ↓             ↓              ↓             ↓             ↓
  knowledge-    llms.txt       robots.txt    feed.json    /news/*
  graph.json    (context)      (directives)  (updates)    (namespace)
  (entities)
```

---

## What's New in v3.0

### MCP Agent Integration (Level 4)
- **Model Context Protocol** - AI agents can now interact with ADP-compliant platforms
- **Tool Advertisement** - `/mcp.json` endpoint declares available tools
- **Agent Declaration** - `/.well-known/agents.json` specifies agent capabilities
- **22 Endpoint Architecture** - Expanded from 20 to 22 endpoints

### New Endpoints (v3.0)
| Endpoint | Purpose |
|----------|---------|
| `/mcp.json` | MCP tool discovery |
| `/.well-known/agents.json` | Agent capabilities |
| `/api/v1/mcp/sse` | SSE transport |
| `/api/v1/mcp/messages` | JSON-RPC handler |

### Previous Features (v2.1)
- **News Namespace** - `/news/*` endpoints for news-specific AI optimization
- **Tiered Content** - `/llms.txt`, `/llms-full.txt`, `/llms-lite.txt`
- **Proof Infrastructure** - Track AI crawler visits and citations
- **HTTP Security Headers** - ETag, Content-Digest, X-Update-Frequency, CORS

---

## Quick Start

### Level 1: Minimal (15 minutes)

Create `/ai-discovery.json` at your website root:

```json
{
  "version": "2.1",
  "generatedAt": "2026-01-08T12:00:00Z",
  "website": {
    "url": "https://example.com",
    "name": "Example Corporation",
    "description": "Leading provider of example products and services"
  },
  "endpoints": {
    "knowledgeGraph": "/knowledge-graph.json",
    "contextDocument": "/llms.txt",
    "crawlerDirectives": "/robots.txt"
  },
  "capabilities": {
    "supportsVersioning": true,
    "supportsIncrementalUpdates": true,
    "updateFrequency": "daily"
  }
}
```

---

### Level 2: Standard (2-4 hours) — **RECOMMENDED**

Implement the core 6 files:

| File | Purpose | Required |
|------|---------|----------|
| `/ai-discovery.json` | Meta-index entry point | **Yes** |
| `/knowledge-graph.json` | Schema.org entity catalog | Recommended |
| `/llms.txt` | Human-readable context | Recommended |
| `/robots.txt` | AI crawler directives | Recommended |
| `/feed.json` | Content updates (JSON Feed) | Optional |
| `/ai-sitemap.xml` | AI-optimized sitemap | Optional |

**See:** [examples/standard/](examples/standard/) for complete templates

---

### Level 3: Advanced - News Publishers (1-2 days)

All Level 2 files plus the news namespace:

```
/news/
├── llms.txt           # News-specific context
├── speakable.json     # Voice assistant content
├── changelog.json     # Version history
└── archive.jsonl      # Historical streaming
```

**See:** [docs/NEWS_NAMESPACE.md](docs/NEWS_NAMESPACE.md)

---

### Level 4: Enterprise - MCP & Citation Tracking

Complete ADP implementation with MCP integration and proof infrastructure:

- **MCP Integration** - AI agents can invoke tools on your platform
- **Tool Advertisement** - `/mcp.json` declares available tools
- **Agent Declaration** - `/.well-known/agents.json` specifies capabilities
- **Crawler Hit Logging** - Track visits from GPTBot, ClaudeBot, PerplexityBot
- **Citation Detection** - Monitor when AI systems cite your content
- **ROI Attribution** - Connect citations back to source content

**See:** [SPECIFICATION.md#10-mcp-integration](SPECIFICATION.md#10-mcp-integration-level-4---optional) | [docs/PROOF_INFRASTRUCTURE.md](docs/PROOF_INFRASTRUCTURE.md)

---

## Complete Endpoint Reference

### Core Endpoints (Required/Recommended)

| Endpoint | Format | Purpose |
|----------|--------|---------|
| `/ai-discovery.json` | JSON | Meta-index (entry point) |
| `/knowledge-graph.json` | JSON-LD | Entity catalog |
| `/llms.txt` | Markdown | AI context document |
| `/robots.txt` | Text | Crawler directives |

### Content Feeds

| Endpoint | Format | Purpose |
|----------|--------|---------|
| `/feed.json` | JSON Feed 1.1 | Content updates |
| `/updates.json` | JSON | Recent changes |
| `/ai-sitemap.xml` | XML | AI-optimized sitemap |
| `/rss.xml` | RSS 2.0 | Traditional feed |

### Tiered Content

| Endpoint | Size | Purpose |
|----------|------|---------|
| `/llms.txt` | ~1.2KB | Standard context |
| `/llms-lite.txt` | ~200 bytes | Minimal overview |
| `/llms-full.txt` | 50KB+ | Comprehensive crawl |

### News Namespace

| Endpoint | Format | Purpose |
|----------|--------|---------|
| `/news/llms.txt` | Markdown | News-specific context |
| `/news/speakable.json` | JSON | Voice assistant content |
| `/news/changelog.json` | JSON | Version history |
| `/news/archive.jsonl` | JSONL | Historical streaming |

### Well-Known & Integration

| Endpoint | Format | Purpose |
|----------|--------|---------|
| `/.well-known/ai.json` | JSON | Standardized discovery |
| `/.well-known/agents.json` | JSON | Agent capabilities (Level 4) |
| `/.well-known/security.txt` | Text | Security contact info |
| `/opensearch.xml` | XML | Browser search plugin |
| `/ai-discovery.md` | Markdown | Human-readable discovery |
| `/api/webhooks/discovery` | JSON | Webhook registration |
| `/api/v1/adp/stats` | JSON | Public crawler statistics |

### MCP Integration (Level 4)

| Endpoint | Format | Purpose |
|----------|--------|---------|
| `/mcp.json` | JSON | MCP tool advertisement |
| `/api/v1/mcp/sse` | SSE | Real-time MCP transport |
| `/api/v1/mcp/messages` | JSON-RPC | MCP message handler |

---

## AI Crawler Support

ADP explicitly supports these AI crawlers in `robots.txt`:

```
# AI Discovery Protocol v2.1 - AI Crawlers Welcomed
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Bytespider
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: Meta-ExternalAgent
Allow: /
```

---

## Reference Implementation

**Live Example:** [Pressonify.ai](https://pressonify.ai)

Test these production endpoints:
- https://pressonify.ai/ai-discovery.json
- https://pressonify.ai/knowledge-graph.json
- https://pressonify.ai/llms.txt
- https://pressonify.ai/llms-full.txt
- https://pressonify.ai/news/llms.txt
- https://pressonify.ai/news/speakable.json
- https://pressonify.ai/feed.json

---

## Documentation

| Document | Description |
|----------|-------------|
| [SPECIFICATION.md](SPECIFICATION.md) | Complete protocol specification |
| [RESULTS.md](RESULTS.md) | **Real citation outcomes (anonymized)** |
| [QUICK_START.md](QUICK_START.md) | Implementation guide |
| [docs/NEWS_NAMESPACE.md](docs/NEWS_NAMESPACE.md) | News publisher guide |
| [docs/PROOF_INFRASTRUCTURE.md](docs/PROOF_INFRASTRUCTURE.md) | Citation tracking |
| [docs/HTTP_HEADERS.md](docs/HTTP_HEADERS.md) | Security headers guide |
| [FAQ.md](FAQ.md) | Frequently asked questions |

---

## Proven Results

ADP isn't just a specification—it's a **proven system** with measurable outcomes.

| Metric | Result |
|--------|--------|
| Average time to first AI citation | **2.4 days** |
| Citation detection rate | **100%** |
| AI crawler visits (30-day sample) | **1,200+** |
| AI platforms citing content | **4** (Perplexity, ChatGPT, Claude, Gemini) |

**Case study highlights:**
- B2B SaaS company: 12 → 847 crawler visits/month, first citation in 18 hours
- E-commerce brand: Cited in direct brand queries within 72 hours
- Healthcare startup: 1,100+ crawler visits/month with FDA approval content

👉 **[View Full Results →](RESULTS.md)** — Anonymized data from real ADP implementations

---

## Framework Examples

| Framework | Location |
|-----------|----------|
| FastAPI (Python) | [examples/fastapi/](examples/fastapi/) |
| Node.js/Express | [examples/nodejs/](examples/nodejs/) |
| Static Site | [examples/static/](examples/static/) |
| Next.js | [examples/nextjs/](examples/nextjs/) |
| Shopify | [examples/shopify/](examples/shopify/) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **3.0** | Jan 2026 | MCP integration, 22 endpoints, agent declaration |
| 2.1 | Jan 2026 | News namespace, 20 endpoints, proof infrastructure |
| 2.0 | Dec 2025 | HTTP headers, capabilities object, 8-factor scoring |
| 1.0 | Nov 2025 | Initial release, 4-file architecture |

**See:** [CHANGELOG.md](CHANGELOG.md) for full history

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- **Issues:** https://github.com/BuddySpuds/AI-Discovery-Protocol/issues
- **Discussions:** https://github.com/BuddySpuds/AI-Discovery-Protocol/discussions
- **Pull Requests:** Welcome for documentation, examples, and spec improvements

---

## License

MIT License - See [LICENSE](LICENSE) for details.

---

## Links

- **Specification:** https://github.com/BuddySpuds/AI-Discovery-Protocol
- **Reference Implementation:** https://pressonify.ai
- **Live Demo:** https://pressonify.ai/ai-discovery.json

---

*AI Discovery Protocol is an open standard maintained by [Pressonify](https://pressonify.ai)*
