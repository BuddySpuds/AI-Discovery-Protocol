# AI Discovery Protocol (ADP) v1.0
## Making Websites Discoverable to AI Systems

**Status:** Draft Specification
**Version:** 1.0.0
**Published:** November 2, 2025
**Author:** Pressonify.ai
**License:** MIT License

---

## Abstract

The AI Discovery Protocol (ADP) is an open standard that enables websites to make their content discoverable and understandable to AI systems (LLMs, search engines, reasoning engines, and AI agents). Unlike traditional SEO which optimizes for keyword-based search crawlers, ADP provides structured, machine-readable metadata specifically designed for AI reasoning systems.

ADP builds upon existing standards (Schema.org, JSON-LD, robots.txt) while introducing novel mechanisms for AI-first content discovery, versioning, and incremental updates.

---

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Design Principles](#design-principles)
3. [Core Architecture](#core-architecture)
4. [Specification](#specification)
   - [4.1 ai-discovery.json (Meta-Index)](#41-ai-discoveryjson-meta-index)
   - [4.2 knowledge-graph.json (Entity Catalog)](#42-knowledge-graphjson-entity-catalog)
   - [4.3 llms.txt (Context Document)](#43-llmstxt-context-document)
   - [4.4 robots.txt (Crawler Directives)](#44-robotstxt-crawler-directives)
5. [Implementation Levels](#implementation-levels)
6. [Examples](#examples)
7. [Security Considerations](#security-considerations)
8. [Future Extensions](#future-extensions)
9. [References](#references)

---

## 1. Problem Statement

### Traditional SEO vs AI Discovery

Traditional search engine optimization (SEO) was designed for keyword-based crawlers that:
- Index HTML pages with minimal semantic understanding
- Rely on keyword matching and backlink analysis
- Use heuristic algorithms (PageRank, etc.)

AI systems (ChatGPT, Claude, Perplexity, Gemini) work fundamentally differently:
- **Query structured entity catalogs** instead of keyword indexes
- **Reason over relationships** between entities
- **Require context windows** optimized for AI processing
- **Need freshness signals** for cache invalidation

### Current Limitations

1. **No standard entry point**: AI systems must guess where to find structured data
2. **HTML overhead**: Pages with navigation, ads, and JavaScript are inefficient to process
3. **No versioning**: AI systems can't detect when content has changed
4. **No entity index**: AI must parse entire sites to discover entities
5. **Scattered metadata**: Schema.org exists but lacks coordination with other discovery files

---

## 2. Design Principles

The AI Discovery Protocol follows these core principles:

### 2.1 Simplicity Over Features
- **Minimal required files**: Only `/ai-discovery.json` is mandatory
- **Progressive enhancement**: Sites can implement features incrementally
- **No complex schemas**: Use existing standards (Schema.org, JSON-LD)

### 2.2 Single Entry Point
- **One canonical file**: AI systems request `/ai-discovery.json` first
- **Discovery from root**: All other files are referenced from the meta-index
- **No guessing**: Clear, predictable structure

### 2.3 Build on Standards
- **Schema.org compatibility**: Use established vocabularies
- **JSON-LD format**: W3C-recommended linked data format
- **HTTP standards**: Standard headers (`Last-Modified`, `Cache-Control`)

### 2.4 Incremental Update Support
- **Versioning**: Track changes to entities and metadata
- **Change logs**: Enable smart re-crawling
- **Timestamps**: RFC 3339 format for all dates

### 2.5 Developer-Friendly
- **JSON format**: Modern, widely supported
- **Clear examples**: Comprehensive documentation
- **Validation tools**: JSON Schema for validation

---

## 3. Core Architecture

### File Structure

```
website.com/
├── ai-discovery.json          # Meta-index (REQUIRED)
├── knowledge-graph.json       # Entity catalog (RECOMMENDED)
├── llms.txt                   # AI-readable context (RECOMMENDED)
└── robots.txt                 # Crawler directives (STANDARD)
```

### Discovery Flow

```
AI System → GET /ai-discovery.json
          ↓
       Parse meta-index
          ↓
       ┌────────────┬──────────────┬─────────────┐
       ↓            ↓              ↓             ↓
  knowledge-   llms.txt      robots.txt    Other
  graph.json                               endpoints
```

---

## 4. Specification

### 4.1 ai-discovery.json (Meta-Index)

**Purpose:** Single entry point that maps all AI discovery resources on the site.

**Location:** `https://example.com/ai-discovery.json`

**HTTP Headers:**
```http
Content-Type: application/json
Cache-Control: public, max-age=3600, stale-while-revalidate=86400
Last-Modified: Sat, 02 Nov 2025 12:00:00 GMT
```

**Schema:**

```json
{
  "$schema": "https://pressonify.ai/schemas/ai-discovery/v1.0.json",
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "website": {
    "url": "https://example.com",
    "name": "Example Corporation",
    "description": "Leading provider of example products and services"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://example.com/knowledge-graph.json",
      "format": "application/ld+json",
      "lastModified": "2025-11-02T11:30:00Z",
      "entityCount": 132,
      "version": "2.1.5"
    },
    "contextDocument": {
      "url": "https://example.com/llms.txt",
      "format": "text/markdown",
      "lastModified": "2025-11-01T10:00:00Z",
      "sections": ["Overview", "Products", "Press Releases", "Contact"]
    },
    "crawlerDirectives": {
      "url": "https://example.com/robots.txt",
      "allowsAI": true
    }
  },
  "capabilities": {
    "supportsVersioning": true,
    "supportsIncrementalUpdates": true,
    "supportsChangeDetection": true,
    "updateFrequency": "daily"
  },
  "contact": {
    "email": "ai-discovery@example.com",
    "issuesUrl": "https://github.com/example/ai-discovery/issues"
  }
}
```

**Required Fields:**
- `version` (string): Semantic version of ai-discovery.json format
- `generatedAt` (string): ISO 8601 timestamp
- `website.url` (string): Canonical URL of the website

**Optional Fields:**
- `endpoints.*`: References to other discovery files
- `capabilities.*`: Feature support flags
- `contact.*`: Technical contact information

---

### 4.2 knowledge-graph.json (Entity Catalog)

**Purpose:** Structured catalog of all entities on the site using Schema.org vocabularies.

**Location:** `https://example.com/knowledge-graph.json`

**HTTP Headers:**
```http
Content-Type: application/ld+json
Cache-Control: public, max-age=3600, stale-while-revalidate=86400
Last-Modified: Sat, 02 Nov 2025 11:30:00 GMT
ETag: "2.1.5"
```

**Schema:**

```json
{
  "@context": "https://schema.org",
  "@type": "KnowledgeGraph",
  "version": "2.1.5",
  "generatedAt": "2025-11-02T11:30:00Z",
  "changeLog": {
    "lastModified": "2025-11-02T11:30:00Z",
    "changes": [
      {
        "timestamp": "2025-11-02T11:30:00Z",
        "entityType": "Product",
        "entityId": "https://example.com/products/widget-pro",
        "changeType": "updated",
        "modifiedFields": ["price", "availability"]
      },
      {
        "timestamp": "2025-11-01T09:15:00Z",
        "entityType": "NewsArticle",
        "entityId": "https://example.com/news/product-launch",
        "changeType": "created"
      }
    ]
  },
  "statistics": {
    "totalEntities": 132,
    "byType": {
      "Organization": 1,
      "Product": 45,
      "NewsArticle": 78,
      "Person": 5,
      "FAQPage": 3
    }
  },
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Example Corporation",
      "url": "https://example.com",
      "logo": "https://example.com/logo.png",
      "sameAs": [
        "https://twitter.com/example",
        "https://linkedin.com/company/example"
      ],
      "contactPoint": {
        "@type": "ContactPoint",
        "contactType": "Customer Service",
        "email": "support@example.com"
      }
    },
    {
      "@type": "Product",
      "@id": "https://example.com/products/widget-pro",
      "name": "Widget Pro",
      "description": "Professional-grade widget",
      "brand": {
        "@id": "https://example.com/#organization"
      },
      "offers": {
        "@type": "Offer",
        "price": "299.00",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock"
      }
    },
    {
      "@type": "NewsArticle",
      "@id": "https://example.com/news/product-launch",
      "headline": "Example Corp Launches Widget Pro",
      "datePublished": "2025-11-01T09:00:00Z",
      "author": {
        "@type": "Organization",
        "@id": "https://example.com/#organization"
      },
      "publisher": {
        "@id": "https://example.com/#organization"
      },
      "url": "https://example.com/news/product-launch"
    }
  ]
}
```

**Required Fields:**
- `@context` (string): Must be `https://schema.org`
- `@type` (string): Must be `KnowledgeGraph`
- `@graph` (array): Array of Schema.org entities

**Recommended Fields:**
- `version` (string): Semantic version for change tracking
- `generatedAt` (string): ISO 8601 timestamp
- `changeLog` (object): Recent changes for incremental updates
- `statistics` (object): Entity counts by type

**Change Types:**
- `created`: New entity added
- `updated`: Existing entity modified
- `deleted`: Entity removed (tombstone record)

---

### 4.3 llms.txt (Context Document)

**Purpose:** Human-readable Markdown document providing context for AI systems.

**Location:** `https://example.com/llms.txt`

**Format:** Markdown with frontmatter metadata

**HTTP Headers:**
```http
Content-Type: text/markdown; charset=utf-8
Cache-Control: public, max-age=86400
Last-Modified: Fri, 01 Nov 2025 10:00:00 GMT
```

**Structure:**

```markdown
---
version: 1.0.0
lastModified: 2025-11-01T10:00:00Z
---

# Example Corporation

> AI-Optimized Content for Large Language Models

## Overview

Example Corporation is a leading provider of professional widgets and widget-related services. Founded in 2020, we serve over 10,000 customers worldwide.

## Products

### Widget Pro
- **Price:** $299 USD
- **Features:** Advanced automation, real-time analytics, API access
- **Use Cases:** Enterprise widget management, scalable deployments

### Widget Lite
- **Price:** $49 USD
- **Features:** Basic automation, simple interface
- **Use Cases:** Small teams, individual users

## Recent Press Releases

### Product Launch: Widget Pro v2.0 (November 1, 2025)
Example Corp today announced Widget Pro v2.0 with AI-powered automation...

Read more: https://example.com/news/product-launch

## Contact

- **Website:** https://example.com
- **Email:** support@example.com
- **Documentation:** https://docs.example.com

---
*Last updated: November 1, 2025*
```

**Best Practices:**
- Use clear headings (H1, H2, H3)
- Include recent updates (press releases, product launches)
- Link to full articles for detailed information
- Keep total length under 100KB (context window limits)
- Update weekly or when major changes occur

---

### 4.4 robots.txt (Crawler Directives)

**Purpose:** Standard robots.txt with AI discovery enhancement.

**Location:** `https://example.com/robots.txt`

**Format:**

```
# AI Discovery Protocol
# Learn more: https://github.com/pressonify/ai-discovery-protocol

# AI-Optimized Endpoints
Allow: /ai-discovery.json
Allow: /knowledge-graph.json
Allow: /llms.txt

# Sitemap
Sitemap: https://example.com/sitemap.xml

# Standard crawler rules
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /
```

**AI-Specific Directives:**
- Explicitly allow AI-optimized endpoints
- Reference AI Discovery Protocol documentation
- List AI crawler user-agents

---

## 5. Implementation Levels

Sites can implement ADP at three levels:

### Level 1: Minimal (Entry Point Only)

**Required:**
- `/ai-discovery.json` with basic metadata

**Benefits:**
- Signals AI-friendly intent
- Provides site overview
- Low implementation effort

**Example:**
```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "website": {
    "url": "https://example.com",
    "name": "Example Corp",
    "description": "Professional widget provider"
  }
}
```

---

### Level 2: Standard (Recommended)

**Required:**
- `/ai-discovery.json` (meta-index)
- `/knowledge-graph.json` (entity catalog)
- `/llms.txt` (context document)

**Benefits:**
- Full AI discoverability
- Structured entity catalog
- Human-readable context
- Competitive advantage

---

### Level 3: Advanced (Future-Proof)

**Required:**
- All Level 2 files
- Versioning in `knowledge-graph.json`
- Change log for incremental updates
- Custom endpoints referenced in `ai-discovery.json`

**Benefits:**
- Incremental crawling support
- Cache invalidation optimization
- Extensibility for future features

---

## 6. Examples

### Example 1: E-commerce Site (Shopify Store)

**ai-discovery.json:**
```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "website": {
    "url": "https://mystore.com",
    "name": "My Awesome Store",
    "description": "Handcrafted artisan products"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://mystore.com/knowledge-graph.json",
      "format": "application/ld+json",
      "entityCount": 250,
      "version": "1.0.0"
    },
    "contextDocument": {
      "url": "https://mystore.com/llms.txt",
      "format": "text/markdown"
    }
  },
  "capabilities": {
    "supportsVersioning": true,
    "updateFrequency": "daily"
  }
}
```

**knowledge-graph.json:**
```json
{
  "@context": "https://schema.org",
  "@type": "KnowledgeGraph",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://mystore.com/#organization",
      "name": "My Awesome Store",
      "url": "https://mystore.com"
    },
    {
      "@type": "Product",
      "@id": "https://mystore.com/products/handmade-mug",
      "name": "Handmade Ceramic Mug",
      "offers": {
        "@type": "Offer",
        "price": "24.99",
        "priceCurrency": "USD"
      }
    }
  ]
}
```

---

### Example 2: SaaS Company (Pressonify.ai)

**ai-discovery.json:**
```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "website": {
    "url": "https://pressonify.ai",
    "name": "Pressonify.ai",
    "description": "AI-powered press release platform with 60-second publishing"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://pressonify.ai/knowledge-graph.json",
      "format": "application/ld+json",
      "lastModified": "2025-11-02T11:30:00Z",
      "entityCount": 132,
      "version": "2.7.1"
    },
    "contextDocument": {
      "url": "https://pressonify.ai/llms.txt",
      "format": "text/markdown",
      "lastModified": "2025-11-01T10:00:00Z"
    },
    "crawlerDirectives": {
      "url": "https://pressonify.ai/robots.txt",
      "allowsAI": true
    }
  },
  "capabilities": {
    "supportsVersioning": true,
    "supportsIncrementalUpdates": true,
    "supportsChangeDetection": true,
    "updateFrequency": "daily"
  },
  "contact": {
    "email": "ai-discovery@pressonify.ai"
  }
}
```

---

### Example 3: Blog/Publisher

**ai-discovery.json:**
```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "website": {
    "url": "https://techblog.com",
    "name": "Tech Blog Daily",
    "description": "Latest technology news and analysis"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://techblog.com/knowledge-graph.json",
      "format": "application/ld+json",
      "entityCount": 500
    },
    "contextDocument": {
      "url": "https://techblog.com/llms.txt",
      "format": "text/markdown"
    }
  }
}
```

**knowledge-graph.json (truncated):**
```json
{
  "@context": "https://schema.org",
  "@type": "KnowledgeGraph",
  "statistics": {
    "totalEntities": 500,
    "byType": {
      "NewsArticle": 450,
      "Person": 30,
      "Organization": 20
    }
  },
  "@graph": [
    {
      "@type": "NewsArticle",
      "@id": "https://techblog.com/ai-trends-2025",
      "headline": "Top AI Trends for 2025",
      "datePublished": "2025-11-01T09:00:00Z",
      "author": {
        "@type": "Person",
        "name": "Jane Smith"
      }
    }
  ]
}
```

---

## 7. Security Considerations

### 7.1 Data Exposure
- **Public by design**: All ADP files are publicly accessible
- **Sensitive data**: Do NOT include private information, credentials, or internal URLs
- **Rate limiting**: Implement rate limits on endpoints to prevent abuse

### 7.2 CORS Headers
```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, HEAD, OPTIONS
```

### 7.3 Content Security
- Validate JSON-LD against Schema.org vocabularies
- Escape user-generated content properly
- Use HTTPS for all endpoints

### 7.4 Denial of Service
- Set maximum file sizes (recommended: 10MB for knowledge-graph.json)
- Implement caching with appropriate TTLs
- Use CDN for static files

---

## 8. Future Extensions

### 8.1 Planned Features (v1.1)
- **Entity pagination**: Support for large knowledge graphs (>10,000 entities)
- **Real-time updates**: WebSocket endpoint for live changes
- **Multi-language support**: Localized entity catalogs

### 8.2 Potential Extensions (v2.0)
- **Entity relationships graph**: Explicit relationship mapping beyond Schema.org
- **Query endpoint**: GraphQL-like query interface
- **Federated discovery**: Cross-domain entity references

### 8.3 Community Contributions
We welcome community feedback and proposals for future extensions. Please submit issues or pull requests to the GitHub repository.

---

## 9. References

### Standards
- [Schema.org](https://schema.org/) - Structured data vocabularies
- [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/) - JSON-based Serialization for Linked Data
- [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html)
- [Sitemaps Protocol](https://www.sitemaps.org/protocol.html)
- [RFC 3339: Date and Time on the Internet](https://www.rfc-editor.org/rfc/rfc3339)

### Related Work
- [llms.txt Proposal](https://llmstxt.org/) by Jeremy Howard (Answer.AI)
- [Google Enterprise Knowledge Graph](https://cloud.google.com/enterprise-knowledge-graph)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) by Anthropic

### Resources
- **GitHub Repository**: https://github.com/pressonify/ai-discovery-protocol
- **JSON Schema**: https://pressonify.ai/schemas/ai-discovery/v1.0.json
- **Validation Tool**: https://pressonify.ai/tools/adp-validator
- **Discussion Forum**: https://github.com/pressonify/ai-discovery-protocol/discussions

---

## License

This specification is released under the **MIT License**.

```
Copyright (c) 2025 Pressonify.ai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Changelog

### Version 1.0.0 (November 2, 2025)
- Initial specification release
- Core architecture: ai-discovery.json, knowledge-graph.json, llms.txt, robots.txt
- Versioning and change detection support
- Three implementation levels (Minimal, Standard, Advanced)
- Comprehensive examples and security guidelines

---

**Published by:** [Pressonify.ai](https://pressonify.ai)
**Contributors:** Robert Porter, Claude (Anthropic)
**Last Updated:** November 2, 2025

*We welcome feedback, contributions, and implementations of this standard. Please join the discussion at our GitHub repository.*
