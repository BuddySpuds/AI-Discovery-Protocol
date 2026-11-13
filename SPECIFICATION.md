# AI Discovery Protocol (ADP) v3.1

## Complete Specification

**Status:** Production Specification
**Version:** 3.1
**Published:** November 13, 2026
**Author:** Pressonify.ai
**License:** MIT License

---

## Table of Contents

1. [Abstract](#1-abstract)
2. [Design Principles](#2-design-principles)
3. [Level 1: Page Copies](#3-level-1-page-copies-required)
4. [Optional Endpoint Specifications](#4-optional-endpoint-specifications)
5. [HTTP Headers](#5-http-headers)
6. [News Namespace](#6-news-namespace)
7. [Security Considerations](#7-security-considerations)
8. [Implementation Levels](#8-implementation-levels)
9. [Measurement](#9-measurement)
10. [MCP Integration (Level 4)](#10-mcp-integration-level-4---optional)
11. [Migration Guide](#11-migration-guide)

---

## 1. Abstract

The AI Discovery Protocol (ADP) is an open standard for publishing a website so
that AI crawlers and agents can read it.

ADP v3.1 is an evidence revision. Request logs from the reference
implementation show that crawlers fetch pages and per-page markdown copies,
and rarely fetch root discovery files ([RESULTS.md](RESULTS.md)). So v3.1:

- makes **page copies** the required level: every content page has a markdown
  copy, linked from the page body and listed in the sitemap;
- moves every root file, including `/ai-discovery.json`, to optional levels;
- defines levels, requirements and endpoints in one machine-readable
  **registry**, `registry/adp-registry.json`, which this document, the audit
  tool and the reference implementation all read.

ADP makes no claim that conformance produces citations. It specifies a way to
publish and a way to measure.

The key words MUST, SHOULD and MAY are used as in RFC 2119.

---

## 2. Design Principles

### 2.1 Follow measured behaviour
- A surface belongs in the required level only if crawlers are observed
  fetching it.
- Each revision states the evidence it rests on and the limits of that
  evidence.

### 2.2 Discovery through links and sitemaps
- Crawlers find content by following links and reading sitemaps. They do not
  probe for a special entry-point file.
- Anything a site wants read MUST be reachable from a page body or a sitemap.

### 2.3 Build on standards
- Markdown for page copies, `robots.txt` (RFC 9309) and the sitemap protocol
  for discovery.
- Schema.org vocabularies and JSON-LD for entities.
- Standard HTTP headers.

### 2.4 One registry
- Levels, page requirements and endpoints are defined once, in
  `registry/adp-registry.json`.
- Tools MUST read the registry rather than carry their own list.

### 2.5 Optional means optional
- Only Level 1 is needed to conform.
- Levels 2 to 4 are independent: a site MAY implement any of them, in any
  order, and MAY skip them all.

---

## 3. Level 1: Page Copies (Required)

### 3.1 Requirements

A **content page** is a page whose text the site wants AI systems to be able
to read and quote: an article, a release, a product page, a reference entry.
The site decides which of its pages are content pages.

For each content page:

<!-- registry:page:start -->
<!-- registry:page:end -->

And for the site:

- `/robots.txt` MUST exist and MUST name at least one sitemap with a
  `Sitemap:` line, or the site MUST serve `/sitemap.xml`.
- That sitemap MUST list the content pages and their markdown copies.

### 3.2 The markdown copy

- **Location.** Any stable URL on the same site. Two common layouts are the
  page URL with `.md` appended (`/blog/our-launch.md`) and a parallel tree
  (`/md/blog/our-launch.md`). The reference implementation uses a parallel
  tree under `/okf/`.
- **Response.** `200`, with `Content-Type: text/markdown` or `text/plain`, in
  UTF-8.
- **Content.** The same content as the page: title, date, author or
  publisher, and the full body text. Navigation, advertising and scripts are
  left out. The copy MUST NOT say anything the page does not.
- **Front matter.** A YAML front matter block MAY carry metadata (title,
  canonical URL of the page, dates, type).
- **Canonical link.** The copy SHOULD name the URL of the page it copies, so a
  reader of the copy can cite the page.

Example copy:

```markdown
---
title: Example Corporation opens a Dublin office
url: https://example.com/news/dublin-office
date: 2026-11-13
type: press-release
---

# Example Corporation opens a Dublin office

Example Corporation today opened an office in Dublin...
```

### 3.3 The link from the page

The page body MUST contain an ordinary, visible `<a href>` link to the copy.
Crawlers that work from extracted body text do not see `<head>` elements or
HTTP headers, so a head link alone is not enough.

```html
<p>For AI agents and developers:
  <a href="/news/dublin-office.md">this page as markdown</a>.</p>
```

The page head SHOULD also carry:

```html
<link rel="alternate" type="text/markdown" href="/news/dublin-office.md">
```

### 3.4 The sitemap listing

Each copy is listed as its own `<url>` entry:

```xml
<url><loc>https://example.com/news/dublin-office</loc></url>
<url><loc>https://example.com/news/dublin-office.md</loc></url>
```

### 3.5 Checking conformance

A page conforms to Level 1 when every required row in section 3.1 holds for
it. A site conforms when all of its content pages do. Because only the site
knows which pages are content pages, an automated audit samples pages from
the sitemap and reports how many of the sample conform.

### 3.6 Request flow

```
Crawler
   |
   +--> GET /robots.txt      (rules, and where the sitemap is)
   +--> GET /sitemap.xml     (pages and their markdown copies)
   +--> GET /news/dublin-office       (the page, with a body link to its copy)
   +--> GET /news/dublin-office.md    (the copy)
```

---

## 4. Optional Endpoint Specifications

The registry lists every endpoint the protocol defines:

<!-- registry:endpoints:start -->
<!-- registry:endpoints:end -->

A site that serves an optional endpoint SHOULD link to it from
`/ai-discovery.json` or `/llms.txt` if it serves either, and MUST keep it
current: a stale file is worse than no file.

Retired paths:

<!-- registry:retired:start -->
<!-- registry:retired:end -->

### 4.1 `/ai-discovery.json` (Optional, Level 2)

A meta-index of the site's machine-readable resources. Versions 1.0 to 3.0
required this file as the single entry point; v3.1 does not, because crawlers
are not observed using it that way.


**Response:**

```json
{
  "version": "3.1",
  "generatedAt": "2026-01-08T12:00:00Z",
  "website": {
    "url": "https://example.com",
    "name": "Example Corporation",
    "description": "Brief description of the website",
    "primaryLanguage": "en",
    "category": "technology"
  },
  "endpoints": {
    "markdownCopies": "/md/index.md",
    "knowledgeGraph": "/knowledge-graph.json",
    "contextDocument": "/llms.txt",
    "contextDocumentFull": "/llms-full.txt",
    "contextDocumentLite": "/llms-lite.txt",
    "crawlerDirectives": "/robots.txt",
    "contentFeed": "/feed.json",
    "recentUpdates": "/updates.json",
    "newsNamespace": "/news/",
    "webhookDiscovery": "/api/v1/webhooks/discovery"
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

### 4.2 `/knowledge-graph.json` (Optional, Level 2)

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

### 4.3 `/llms.txt` (Optional, Level 2)

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

### 4.4 `/feed.json` (Optional, Level 3)

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

### 4.5 `/updates.json` (Optional, Level 3)

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

### 4.6 `/ai-sitemap.xml` (Retired in v3.1)

Retired. List pages and their markdown copies in the standard sitemap instead. The format below is kept for sites that still serve the file.

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

### 4.7 `/.well-known/ai.json` (Optional, Level 2)

Standardized well-known location for AI discovery.

**Response:** Same format as `/ai-discovery.json`

---

### 4.8 `/opensearch.xml` (Optional, Level 2)

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

### 4.9 `/api/v1/webhooks/discovery` (Optional, Level 3)

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

Markdown copies and optional endpoints SHOULD include these headers:

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

<!-- registry:levels:start -->
<!-- registry:levels:end -->

Only Level 1 is required. Levels 2 to 4 are independent of each other.

| Level | What to build | Evidence from the reference site (30 days to 12 November 2026) |
|---|---|---|
| 1 | Markdown copies, body links, sitemap listing | Copies drew 23.9% of crawler requests; `robots.txt` and sitemaps 4.6% |
| 2 | `/llms.txt`, `/ai-discovery.json`, `/knowledge-graph.json` and related files | All Level 2 files together: under 1% |
| 3 | Feeds and the news namespace | All Level 3 files together: under 1% |
| 4 | MCP manifest, agent declaration, statistics endpoint | 3 requests |

The optional levels are kept because they are cheap to serve once built and
crawler behaviour changes. A site SHOULD implement Level 1 first and SHOULD
measure (section 9) before investing in the others.

---

## 9. Measurement

A site SHOULD measure which crawlers request which surfaces. Without that, no
one can tell whether any part of this protocol is being read.

### 9.1 Crawler request logging

For every request whose user agent matches a known AI or search crawler, log:

- the crawler name and operator;
- the path requested, and the response status;
- the `Accept` header, which shows whether the client asked for markdown;
- the time.

Group paths by level using the registry: markdown copies, core files
(`robots.txt`, sitemaps), each optional endpoint, and ordinary pages.

```python
def log_crawler_request(request, crawler):
    record({
        "crawler": crawler.name,
        "operator": crawler.operator,
        "path": request.path,
        "status": response.status,
        "accept": request.headers.get("Accept", "")[:200],
        "time": utcnow(),
    })
```

### 9.2 Verifying the crawler

A user agent is free text and is forged in practice. Where an operator
publishes the address ranges its crawler uses, a site SHOULD check the
request address against them and record one of three outcomes: verified,
failed, or no published ranges. "No published ranges" MUST NOT be read as
"fake".

### 9.3 Separating kinds of crawler

Report index and training crawlers separately from fetchers that act for a
person asking a question (for example ChatGPT-User). They behave differently,
and only the second kind shows that content was fetched to answer someone.

### 9.4 Citations

Whether an AI system cites a page is a separate question from whether its
crawler fetched it. A site MAY check by asking AI systems questions and
recording which sources they cite; see
[docs/PROOF_INFRASTRUCTURE.md](docs/PROOF_INFRASTRUCTURE.md). A citation
count MUST state the questions asked, the systems asked and the date.

### 9.5 Publishing results

A site MAY publish its grouped counts, as [RESULTS.md](RESULTS.md) does for
the reference implementation, and MAY serve them at `/api/v1/adp/stats`.

---

## 10. MCP Integration (Level 4 - Optional)

Level 4 extends ADP from passive discovery to active interaction via the **Model Context Protocol (MCP)**. This enables AI agents to not just find your content, but to interact with your platform programmatically.

> **Note:** MCP integration is entirely optional. Implementations at Levels 1-3 remain fully compliant without MCP support.

### 10.1 Overview

| Level | Capability | AI Interaction |
|-------|------------|----------------|
| 1-3 | Discovery | Read-only |
| 4 | Agent Integration | Read + Execute |

**What MCP Enables:**
- AI agents can invoke tools on your platform
- Structured tool schemas for type-safe interactions
- Real-time communication via Server-Sent Events (SSE)
- Authentication for sensitive operations

---

### 10.2 `/mcp.json` Endpoint

Advertises available MCP tools and transport options.

**Response:**

```json
{
  "version": "1.0",
  "name": "example-platform",
  "description": "Example platform with AI agent tools",
  "transport": {
    "type": "sse",
    "url": "/api/v1/mcp/sse"
  },
  "tools": [
    {
      "name": "search_content",
      "description": "Search platform content by query",
      "inputSchema": {
        "type": "object",
        "properties": {
          "query": {
            "type": "string",
            "description": "Search query"
          },
          "limit": {
            "type": "integer",
            "default": 10
          }
        },
        "required": ["query"]
      }
    },
    {
      "name": "get_content",
      "description": "Retrieve content by ID",
      "inputSchema": {
        "type": "object",
        "properties": {
          "content_id": {
            "type": "string",
            "description": "Content identifier"
          }
        },
        "required": ["content_id"]
      }
    }
  ],
  "resources": [
    {
      "uri": "content://recent",
      "name": "Recent Content",
      "description": "List of recently published content"
    }
  ]
}
```

**Headers:**
```
Content-Type: application/json
Cache-Control: public, max-age=3600
```

---

### 10.3 `/.well-known/agents.json` Endpoint

Declares agent capabilities and authentication requirements.

**Response:**

```json
{
  "version": "1.0",
  "agents": [
    {
      "name": "content-assistant",
      "description": "AI assistant for content discovery and creation",
      "capabilities": ["search", "read", "create"],
      "authentication": "optional",
      "rate_limit": "100/hour"
    },
    {
      "name": "analytics-agent",
      "description": "AI agent for analytics and reporting",
      "capabilities": ["read", "analyze"],
      "authentication": "required",
      "rate_limit": "60/hour"
    }
  ],
  "mcp_endpoint": "/mcp.json",
  "documentation": "https://example.com/docs/agents"
}
```

**Authentication Values:**
- `none` - No authentication required
- `optional` - Authentication enhances capabilities
- `required` - Must authenticate to use

---

### 10.4 Transport Options

#### Server-Sent Events (SSE) - Recommended

```
GET /api/v1/mcp/sse
Accept: text/event-stream
```

SSE provides:
- Real-time bidirectional communication
- Automatic reconnection
- Works through firewalls and proxies

#### JSON-RPC Messages

```
POST /api/v1/mcp/messages
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "search_content",
    "arguments": {"query": "example"}
  },
  "id": 1
}
```

---

### 10.5 Implementation Notes

1. **MCP is OPTIONAL** - Only implement if you want AI agents to perform actions
2. **SSE is recommended** - Better for real-time interactions than polling
3. **Authentication required for writes** - Read operations can be public
4. **Rate limiting strongly recommended** - Protect against abuse
5. **Log all tool invocations** - Track usage for analytics

**Reference:** [Model Context Protocol Specification](https://modelcontextprotocol.io)

---

## 11. Migration Guide

### From v3.0 to v3.1

v3.1 changes what is required, so a v3.0 site is not automatically a v3.1
Level 1 site.

1. **Add a markdown copy for each content page** (section 3.2).
2. **Link each copy from its page body**, and add the head link (section 3.3).
3. **List the copies in your sitemap** (section 3.4).
4. **Keep or drop root files as you prefer.** `/ai-discovery.json`,
   `/llms.txt` and `/knowledge-graph.json` are now optional. If you keep
   `/ai-discovery.json`, set `"version": "3.1"` and add a pointer to an index
   of your markdown copies.
5. **Replace `/ai-sitemap.xml`** with entries in the standard sitemap.
6. **Start logging** crawler requests by path (section 9).

### From v2.1 to v3.0

1. **Update version number**
   ```json
   "version": "3.0"
   ```

2. **(Optional) Add MCP endpoints** if implementing Level 4:
   - `/mcp.json` - Tool advertisement
   - `/.well-known/agents.json` - Agent capabilities
   - `/api/v1/mcp/sse` - SSE transport
   - `/api/v1/mcp/messages` - JSON-RPC handler

3. **No breaking changes** - v3.0 is backwards compatible with v2.1

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

The optional endpoints in v3.1 keep the v3.0 formats, which were backwards compatible with v2.1 and v1.0:
- v2.1 clients can read v3.0 responses (ignore MCP fields)
- v3.0 servers can serve v2.1 clients (core fields unchanged)
- MCP endpoints are optional - not required for compliance
- v1.0 clients can read v3.0 responses (ignore new fields)

---

## References

- [Schema.org](https://schema.org) - Vocabulary standard
- [JSON-LD](https://json-ld.org) - Linked data format
- [JSON Feed](https://jsonfeed.org) - Feed format
- [robots.txt](https://www.rfc-editor.org/rfc/rfc9309) - Crawler directives (RFC 9309)
- [Sitemaps](https://www.sitemaps.org/protocol.html) - Sitemap protocol
- [llms.txt](https://llmstxt.org) - Context document format
- [HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching) - Cache headers

---

## License

This specification is released under the MIT License.

---

*AI Discovery Protocol v3.0 - January 2026*
*Maintained by [Pressonify](https://pressonify.ai)*
