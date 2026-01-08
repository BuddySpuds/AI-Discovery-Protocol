# AI Discovery Protocol (ADP) v2.1

## Complete Specification

**Status:** Production Specification
**Version:** 2.1
**Published:** January 8, 2026
**Author:** Pressonify.ai
**License:** MIT License

---

## Table of Contents

1. [Abstract](#1-abstract)
2. [Design Principles](#2-design-principles)
3. [Core Architecture](#3-core-architecture)
4. [Endpoint Specifications](#4-endpoint-specifications)
5. [HTTP Headers](#5-http-headers)
6. [News Namespace](#6-news-namespace)
7. [Security Considerations](#7-security-considerations)
8. [Implementation Levels](#8-implementation-levels)
9. [Proof Infrastructure](#9-proof-infrastructure)
10. [Migration Guide](#10-migration-guide)

---

## 1. Abstract

The AI Discovery Protocol (ADP) is an open standard that enables websites to make their content discoverable and understandable to AI systems (LLMs, AI search engines, reasoning engines, and AI agents). Unlike traditional SEO which optimizes for keyword-based search crawlers, ADP provides structured, machine-readable metadata specifically designed for AI reasoning systems.

ADP v2.1 introduces:
- **17 endpoint architecture** (expanded from 4 in v1.0)
- **News namespace** for publishers and news content
- **Proof infrastructure** for tracking AI crawler visits and citations
- **HTTP security headers** for cache validation and integrity verification
- **Tiered content** for different AI system needs

---

## 2. Design Principles

### 2.1 Single Entry Point
- AI systems request `/ai-discovery.json` first
- All other endpoints are referenced from this meta-index
- Predictable, no guessing required

### 2.2 Build on Standards
- Schema.org vocabularies for entities
- JSON-LD format (W3C-recommended)
- Standard HTTP headers

### 2.3 Progressive Enhancement
- Only `/ai-discovery.json` is strictly required
- Additional endpoints provide incremental value
- Sites can implement features at their own pace

### 2.4 AI-First Design
- Content sized for context windows
- Structured for AI extraction
- Freshness signals for cache management

---

## 3. Core Architecture

### 3.1 File Structure

```
website.com/
├── ai-discovery.json          # Meta-index (REQUIRED)
├── knowledge-graph.json       # Entity catalog (Recommended)
├── llms.txt                   # Context document (Recommended)
├── llms-lite.txt             # Minimal context (Optional)
├── llms-full.txt             # Comprehensive context (Optional)
├── robots.txt                 # Crawler directives (Recommended)
├── feed.json                  # JSON Feed (Optional)
├── updates.json               # Recent changes (Optional)
├── ai-sitemap.xml            # AI sitemap (Optional)
├── opensearch.xml            # Search plugin (Optional)
├── .well-known/
│   └── ai.json               # Well-known discovery (Optional)
├── news/                      # News namespace (Optional)
│   ├── llms.txt              # News context
│   ├── speakable.json        # Voice content
│   ├── changelog.json        # Version history
│   └── archive.jsonl         # Historical streaming
└── api/
    └── webhooks/
        └── discovery          # Webhook registration (Optional)
```

### 3.2 Request Flow

```
AI System
    │
    ▼
GET /ai-discovery.json
    │
    ├──► Parse meta-index
    │
    ▼
Discover available endpoints
    │
    ├──► /knowledge-graph.json (entities)
    ├──► /llms.txt (context)
    ├──► /feed.json (updates)
    └──► /news/* (news content)
```

---

## 4. Endpoint Specifications

### 4.1 `/ai-discovery.json` (REQUIRED)

The single entry point for AI discovery. All other endpoints are referenced here.

**Response:**

```json
{
  "version": "2.1",
  "generatedAt": "2026-01-08T12:00:00Z",
  "website": {
    "url": "https://example.com",
    "name": "Example Corporation",
    "description": "Brief description of the website",
    "primaryLanguage": "en",
    "category": "technology"
  },
  "endpoints": {
    "knowledgeGraph": "/knowledge-graph.json",
    "contextDocument": "/llms.txt",
    "contextDocumentFull": "/llms-full.txt",
    "contextDocumentLite": "/llms-lite.txt",
    "crawlerDirectives": "/robots.txt",
    "contentFeed": "/feed.json",
    "recentUpdates": "/updates.json",
    "aiSitemap": "/ai-sitemap.xml",
    "newsNamespace": "/news/",
    "webhookDiscovery": "/api/webhooks/discovery"
  },
  "capabilities": {
    "supportsVersioning": true,
    "supportsIncrementalUpdates": true,
    "supportsChangeDetection": true,
    "updateFrequency": "daily"
  },
  "contact": {
    "email": "ai-support@example.com",
    "issuesUrl": "https://github.com/example/issues"
  }
}
```

**Headers:**
```
Content-Type: application/json
ETag: W/"abc123"
Cache-Control: public, max-age=3600
X-Update-Frequency: daily
```

---

### 4.2 `/knowledge-graph.json` (Recommended)

Schema.org entity catalog in JSON-LD format.

**Response:**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Example Corporation",
      "url": "https://example.com",
      "logo": "https://example.com/logo.png",
      "description": "Leading provider of example services",
      "sameAs": [
        "https://twitter.com/example",
        "https://linkedin.com/company/example"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "name": "Example",
      "url": "https://example.com",
      "publisher": {"@id": "https://example.com/#organization"}
    },
    {
      "@type": "Product",
      "@id": "https://example.com/product#product",
      "name": "Example Product",
      "description": "Our flagship product",
      "offers": {
        "@type": "Offer",
        "price": "99.00",
        "priceCurrency": "USD"
      }
    }
  ],
  "adp:version": "2.7.1",
  "adp:entityCount": 3,
  "adp:lastUpdated": "2026-01-08T12:00:00Z"
}
```

---

### 4.3 `/llms.txt` (Recommended)

Human-readable Markdown context document optimized for AI processing.

**Format:** Markdown
**Size:** 1-2KB (standard), 50KB+ (full), 200 bytes (lite)

**Example:**

```markdown
# Example Corporation

> Leading provider of example services since 2020

## Overview

Example Corporation helps businesses achieve their goals through innovative solutions.

## Products

- **Product A** - Description of product A
- **Product B** - Description of product B

## Contact

- Website: https://example.com
- Email: hello@example.com

---
*AI Discovery Protocol v2.1 | Updated: 2026-01-08*
```

---

### 4.4 `/feed.json` (Optional)

JSON Feed v1.1 format for content updates.

**Response:**

```json
{
  "version": "https://jsonfeed.org/version/1.1",
  "title": "Example Corporation Updates",
  "home_page_url": "https://example.com",
  "feed_url": "https://example.com/feed.json",
  "description": "Latest updates from Example Corporation",
  "items": [
    {
      "id": "https://example.com/post/123",
      "url": "https://example.com/post/123",
      "title": "New Product Launch",
      "content_text": "We're excited to announce...",
      "date_published": "2026-01-08T12:00:00Z",
      "authors": [{"name": "Example Team"}]
    }
  ]
}
```

---

### 4.5 `/updates.json` (Optional)

Recent content changes for incremental crawling.

**Response:**

```json
{
  "version": "2.1",
  "generatedAt": "2026-01-08T12:00:00Z",
  "updateWindow": "7d",
  "updates": [
    {
      "url": "/post/123",
      "type": "created",
      "timestamp": "2026-01-08T12:00:00Z",
      "title": "New Post"
    },
    {
      "url": "/product/456",
      "type": "modified",
      "timestamp": "2026-01-07T10:00:00Z",
      "changeType": "price_update"
    }
  ]
}
```

---

### 4.6 `/ai-sitemap.xml` (Optional)

AI-optimized XML sitemap with priority hints.

**Response:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:ai="https://ai-discovery-protocol.org/sitemap">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2026-01-08</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
    <ai:content-type>homepage</ai:content-type>
  </url>
  <url>
    <loc>https://example.com/products</loc>
    <lastmod>2026-01-07</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
    <ai:content-type>catalog</ai:content-type>
  </url>
</urlset>
```

---

### 4.7 `/.well-known/ai.json` (Optional)

Standardized well-known location for AI discovery.

**Response:** Same format as `/ai-discovery.json`

---

### 4.8 `/opensearch.xml` (Optional)

Browser search plugin integration.

**Response:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
  <ShortName>Example</ShortName>
  <Description>Search Example Corporation</Description>
  <Url type="text/html" template="https://example.com/search?q={searchTerms}"/>
  <Image>https://example.com/favicon.ico</Image>
</OpenSearchDescription>
```

---

### 4.9 `/api/webhooks/discovery` (Optional)

Webhook registration endpoint for real-time updates.

**Response:**

```json
{
  "version": "2.1",
  "webhooks": {
    "contentUpdates": {
      "url": "/api/webhooks/content",
      "events": ["content.created", "content.updated", "content.deleted"],
      "format": "json"
    },
    "indexNow": {
      "url": "/api/webhooks/indexnow",
      "events": ["index.requested"],
      "format": "json"
    }
  },
  "documentation": "https://example.com/docs/webhooks"
}
```

---

## 5. HTTP Headers

All ADP endpoints SHOULD include these headers:

### 5.1 Required Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `Content-Type` | Media type | `application/json` |
| `ETag` | Cache validation | `W/"abc123"` |

### 5.2 Recommended Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `Content-Digest` | Integrity verification | `sha-256=base64hash` |
| `X-Update-Frequency` | Crawler scheduling | `daily`, `weekly`, `monthly` |
| `Cache-Control` | Caching directives | `public, max-age=3600` |
| `Last-Modified` | Last update timestamp | `Wed, 08 Jan 2026 12:00:00 GMT` |

### 5.3 CORS Headers

For cross-origin AI tool access:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

---

## 6. News Namespace

The `/news/` namespace provides specialized endpoints for news publishers and content sites.

### 6.1 `/news/llms.txt`

News-specific context document focusing on recent content.

**Example:**

```markdown
# Example News

> Breaking news and updates from Example Corporation

## Recent Headlines

1. **New Product Launch** (Jan 8, 2026)
   We announced our latest product today...

2. **Q4 2025 Results** (Jan 5, 2026)
   Record revenue of $10M...

## Categories

- Technology
- Business
- Product Updates

---
*AI Discovery Protocol v2.1 | News Feed*
```

---

### 6.2 `/news/speakable.json`

Voice assistant-optimized content using Schema.org Speakable.

**Response:**

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".headline", ".summary"]
  },
  "items": [
    {
      "headline": "New Product Launch",
      "speakableText": "Example Corporation announced a new product today. The product features...",
      "url": "https://example.com/news/product-launch",
      "datePublished": "2026-01-08T12:00:00Z"
    }
  ]
}
```

---

### 6.3 `/news/changelog.json`

Platform version history and updates.

**Response:**

```json
{
  "version": "2.1",
  "platform": "Example Platform",
  "changelog": [
    {
      "version": "2.1.0",
      "date": "2026-01-08",
      "changes": [
        "Added news namespace",
        "Improved AI crawler support",
        "New speakable content endpoint"
      ]
    },
    {
      "version": "2.0.0",
      "date": "2025-12-01",
      "changes": [
        "HTTP security headers",
        "Capabilities object",
        "8-factor scoring"
      ]
    }
  ]
}
```

---

### 6.4 `/news/archive.jsonl`

Historical content in JSONL streaming format for efficient processing.

**Response:**

```
{"id":"123","title":"Post 1","date":"2026-01-08","url":"/news/post-1"}
{"id":"124","title":"Post 2","date":"2026-01-07","url":"/news/post-2"}
{"id":"125","title":"Post 3","date":"2026-01-06","url":"/news/post-3"}
```

---

## 7. Security Considerations

### 7.1 Content Integrity

Use `Content-Digest` header with SHA-256 hash:

```
Content-Digest: sha-256=X48E9qOokqqrvdts8nOJRJN3OWDUoyWxBf7kbu9DBPE=
```

### 7.2 Rate Limiting

Implement rate limiting for API endpoints:
- Recommended: 60 requests/minute per IP
- Return `429 Too Many Requests` when exceeded

### 7.3 Authentication (Optional)

For private/premium content:
- Use Bearer tokens in `Authorization` header
- Document authentication in `/ai-discovery.json`

### 7.4 robots.txt Directives

Always honor `robots.txt` directives. ADP-compliant sites should explicitly allow AI crawlers:

```
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

---

## 8. Implementation Levels

### Level 1: Minimal
- `/ai-discovery.json` only
- 15 minutes to implement

### Level 2: Standard (Recommended)
- `/ai-discovery.json`
- `/knowledge-graph.json`
- `/llms.txt`
- `/robots.txt`
- 2-4 hours to implement

### Level 3: Advanced
- All Level 2 files
- `/feed.json`
- `/updates.json`
- HTTP security headers
- 1-2 days to implement

### Level 4: Enterprise
- All Level 3 files
- News namespace (`/news/*`)
- Proof infrastructure
- Citation tracking
- 1-2 weeks to implement

---

## 9. Proof Infrastructure

### 9.1 Crawler Hit Logging

Track visits from AI crawlers to measure discoverability:

**Tracked Crawlers:**
- GPTBot (OpenAI)
- ClaudeBot (Anthropic)
- PerplexityBot (Perplexity)
- Google-Extended (Google AI)
- Amazonbot (Amazon)
- Bytespider (ByteDance)
- cohere-ai (Cohere)
- Meta-ExternalAgent (Meta)

**Implementation:**
```python
AI_CRAWLERS = [
    "GPTBot", "ClaudeBot", "PerplexityBot",
    "Google-Extended", "Amazonbot", "anthropic-ai"
]

def log_crawler_hit(request):
    user_agent = request.headers.get("User-Agent", "")
    for crawler in AI_CRAWLERS:
        if crawler.lower() in user_agent.lower():
            # Log to analytics
            track_event("adp_crawler_hit", {
                "crawler": crawler,
                "endpoint": request.path,
                "timestamp": datetime.utcnow()
            })
```

### 9.2 Citation Detection

Monitor when AI systems cite your content:

**Detection Methods:**
1. **Query-based**: Search AI platforms for your brand/content
2. **API-based**: Use Perplexity API for citation scanning
3. **Manual verification**: Periodic spot checks

**Metrics:**
- Total citations per period
- Citations by platform (ChatGPT, Perplexity, Claude)
- Time-to-citation (publish → first cite)
- Citation rate (citations / published content)

### 9.3 ROI Attribution

Connect citations back to source content:

```json
{
  "citation": {
    "id": "cite_123",
    "platform": "perplexity",
    "query": "best press release platform",
    "citedUrl": "https://example.com/post/123",
    "discoveredAt": "2026-01-08T12:00:00Z"
  },
  "attribution": {
    "sourceContentId": "post_123",
    "publishedAt": "2026-01-05T10:00:00Z",
    "timeToCitation": "3 days",
    "confidence": 0.95
  }
}
```

---

## 10. Migration Guide

### From v1.0 to v2.1

1. **Update version number**
   ```json
   "version": "2.1"
   ```

2. **Add capabilities object**
   ```json
   "capabilities": {
     "supportsVersioning": true,
     "supportsIncrementalUpdates": true,
     "updateFrequency": "daily"
   }
   ```

3. **Add HTTP headers** to all endpoints

4. **Optionally add** news namespace and proof infrastructure

### Backwards Compatibility

ADP v2.1 is backwards compatible with v1.0:
- v1.0 clients can read v2.1 responses (ignore new fields)
- v2.1 servers can serve v1.0 clients (core fields unchanged)

---

## References

- [Schema.org](https://schema.org) - Vocabulary standard
- [JSON-LD](https://json-ld.org) - Linked data format
- [JSON Feed](https://jsonfeed.org) - Feed format
- [robots.txt](https://www.robotstxt.org) - Crawler directives
- [HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching) - Cache headers

---

## License

This specification is released under the MIT License.

---

*AI Discovery Protocol v2.1 - January 2026*
*Maintained by [Pressonify](https://pressonify.ai)*
