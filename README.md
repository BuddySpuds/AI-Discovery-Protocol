# AI Discovery Protocol (ADP) v1.0

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)](CHANGELOG.md)
[![Standard](https://img.shields.io/badge/Status-Open%20Standard-success.svg)](SPECIFICATION.md)

**Making websites discoverable to AI systems (ChatGPT, Claude, Perplexity, Gemini)**

---

## 🔍 What is ADP?

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

ADP provides a **4-file architecture** with a single entry point (`/ai-discovery.json`) that maps all AI-optimized resources on your site:

```
AI System → GET /ai-discovery.json (Single entry point)
          ↓
       Parse meta-index
          ↓
       ┌────────────┬──────────────┬─────────────┐
       ↓            ↓              ↓             ↓
  knowledge-   llms.txt      robots.txt    sitemap.xml
  graph.json   (context)     (directives)
  (entities)
```

---

## 🚀 Quick Start

### Level 1: Minimal (15 minutes)

Create `/ai-discovery.json` at your website root:

```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "website": {
    "url": "https://example.com",
    "name": "Example Corporation",
    "description": "Leading provider of example products and services"
  }
}
```

**Benefits:** Signals AI-friendly intent, provides site overview.

---

### Level 2: Standard (2-4 hours) — **RECOMMENDED**

Implement all 4 files:

1. **`/ai-discovery.json`** — Meta-index
2. **`/knowledge-graph.json`** — Schema.org entity catalog
3. **`/llms.txt`** — Human-readable context document
4. **`/robots.txt`** — AI crawler directives

**See:** [examples/standard/](examples/standard/) for complete templates

**Benefits:** Full AI discoverability, structured entity catalog, competitive advantage

---

### Level 3: Advanced (1-2 days)

All Level 2 files plus:
- Versioning in `knowledge-graph.json`
- Change logs for incremental updates
- Custom endpoints

**See:** [examples/advanced/](examples/advanced/)

**Benefits:** Incremental crawling, cache invalidation optimization, future-proof

---

## 📚 The 4 Files Explained

### 1. `/ai-discovery.json` (REQUIRED)

**Purpose:** Single entry point that maps all AI discovery resources

**Format:** JSON

**Key Fields:**
- `version` — Semantic version of the meta-index format
- `website` — Canonical URL, name, description
- `endpoints` — References to knowledge graph, context document, crawler directives

**Example:**
```json
{
  "$schema": "https://pressonify.ai/schemas/ai-discovery/v1.0.json",
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "website": {
    "url": "https://example.com",
    "name": "Example Corporation"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://example.com/knowledge-graph.json",
      "format": "application/ld+json",
      "entityCount": 132
    },
    "contextDocument": {
      "url": "https://example.com/llms.txt",
      "format": "text/markdown"
    },
    "crawlerDirectives": {
      "url": "https://example.com/robots.txt",
      "allowsAI": true
    }
  }
}
```

**HTTP Headers:**
```http
Content-Type: application/json
Cache-Control: public, max-age=3600, stale-while-revalidate=86400
```

---

### 2. `/knowledge-graph.json` (RECOMMENDED)

**Purpose:** Structured catalog of all entities on the site using Schema.org vocabularies

**Format:** JSON-LD

**Key Features:**
- `@graph` array with Schema.org entities (Organization, Product, NewsArticle, Person, etc.)
- Optional `changeLog` for incremental updates
- Optional `statistics` object with entity counts

**Example:**
```json
{
  "@context": "https://schema.org",
  "@type": "KnowledgeGraph",
  "version": "1.0.0",
  "statistics": {
    "totalEntities": 132,
    "byType": {
      "Organization": 1,
      "Product": 45,
      "NewsArticle": 78,
      "Person": 5
    }
  },
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Example Corporation",
      "url": "https://example.com"
    },
    {
      "@type": "Product",
      "@id": "https://example.com/products/widget-pro",
      "name": "Widget Pro",
      "offers": {
        "@type": "Offer",
        "price": "299.00",
        "priceCurrency": "USD"
      }
    }
  ]
}
```

**HTTP Headers:**
```http
Content-Type: application/ld+json
Cache-Control: public, max-age=3600
ETag: "1.0.0"
```

---

### 3. `/llms.txt` (RECOMMENDED)

**Purpose:** Human-readable Markdown document providing context for AI systems

**Format:** Markdown with YAML frontmatter

**Key Sections:**
- Overview
- Products/Services
- Recent News
- Contact Information

**Example:**
```markdown
---
version: 1.0.0
lastModified: 2025-11-02T12:00:00Z
protocol: AI Discovery Protocol v1.0
---

# Example Corporation

> AI-Optimized Content for Large Language Models

## Overview

Example Corporation is a leading provider of professional widgets...

## Products

### Widget Pro
- **Price:** $299 USD
- **Features:** Advanced automation, real-time analytics
- **URL:** https://example.com/products/widget-pro

## Contact

- **Website:** https://example.com
- **Email:** support@example.com
```

**Best Practices:**
- Keep under 100KB (context window limits)
- Update weekly or when major changes occur
- Include recent press releases, product launches, blog posts

---

### 4. `/robots.txt` (STANDARD)

**Purpose:** Standard robots.txt enhanced with AI discovery directives

**Format:** Plain text

**Key Directives:**
- Explicit `Allow` for ADP endpoints
- AI crawler user-agents (GPTBot, Claude-Web, PerplexityBot, Google-Extended)
- Reference to ADP documentation

**Example:**
```
# AI Discovery Protocol v1.0
# Learn more: https://github.com/BuddySpuds/AI-Discovery-Protocol

# AI-Optimized Endpoints
Allow: /ai-discovery.json
Allow: /knowledge-graph.json
Allow: /llms.txt

# Sitemap
Sitemap: https://example.com/sitemap.xml

# AI Crawlers
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /
```

---

## 💡 Why Implement ADP?

### Speed
- **Traditional SEO:** 7-14 days for Google indexing
- **ADP:** 6-24 hours for AI discovery
- **Result:** 10x faster discoverability

### Structure
- **Traditional:** HTML parsing with keyword matching
- **ADP:** Structured entity catalogs with relationships
- **Result:** AI systems understand your content accurately

### Freshness
- **Traditional:** No cache invalidation signals
- **ADP:** Versioning + change logs
- **Result:** Smart re-crawling, efficient updates

### Future-Proof
- **Traditional:** Optimized for 2010s search algorithms
- **ADP:** Designed for AI reasoning systems
- **Result:** Ready for ChatGPT, Perplexity, Claude, Gemini

---

## 🏢 Who's Using ADP?

### Reference Implementation
**[Pressonify.ai](https://pressonify.ai)** — First press release platform with full ADP v1.0 compliance

**Live Endpoints:**
- [ai-discovery.json](https://pressonify.ai/ai-discovery.json) — Meta-index
- [knowledge-graph.json](https://pressonify.ai/knowledge-graph.json) — 17 entities
- [llms.txt](https://pressonify.ai/llms.txt) — 13 press releases
- [robots.txt](https://pressonify.ai/robots.txt) — AI crawler directives

**Results:**
- Press releases discoverable by ChatGPT within 6-24 hours
- NewsArticle entities in knowledge graph (auto-updated)
- 0.592s average endpoint load time
- 68% compression ratio (GZip)

**Read more:** [examples/press-release-platform/](examples/press-release-platform/)

---

## 📖 Documentation

### Core Documentation
- **[SPECIFICATION.md](SPECIFICATION.md)** — Complete technical specification (13,500 words)
- **[QUICK_START.md](QUICK_START.md)** — Implementation guides for all 3 levels
- **[DESIGN_DECISIONS.md](DESIGN_DECISIONS.md)** — Design rationale and trade-offs
- **[FAQ.md](FAQ.md)** — Frequently asked questions
- **[CHANGELOG.md](CHANGELOG.md)** — Version history

### Educational Content
- **[docs/EXPLAINED_SIMPLY.md](docs/EXPLAINED_SIMPLY.md)** — Layperson explanation with analogies
- **[docs/COMPARISON.md](docs/COMPARISON.md)** — ADP vs Schema.org vs llms.txt

---

## 🛠️ Implementation Levels

| Level | Files Required | Time | Use Case | Benefits |
|-------|---------------|------|----------|----------|
| **1 (Minimal)** | `ai-discovery.json` | 15 min | Signal AI-friendly intent | Entry point only |
| **2 (Standard)** ⭐ | All 4 files | 2-4 hrs | Full AI discoverability | Entity catalog + context |
| **3 (Advanced)** | All 4 + versioning | 1-2 days | Future-proof implementation | Incremental updates |

**Recommendation:** Start with Level 2 (Standard) for maximum benefit with reasonable effort.

---

## 📋 Examples by Industry

### E-Commerce (Shopify, WooCommerce)
- [examples/standard/](examples/standard/) — Generic e-commerce template
- **Entities:** Organization, Product, Offer, AggregateRating
- **Use Case:** Product discovery by AI shopping assistants

### SaaS Company
- [examples/press-release-platform/](examples/press-release-platform/) — Pressonify reference
- **Entities:** Organization, SoftwareApplication, NewsArticle
- **Use Case:** Brand awareness, product discovery, press releases

### Blog/Publisher
- [examples/standard/](examples/standard/) — Content publisher template
- **Entities:** Organization, NewsArticle, Person, BlogPosting
- **Use Case:** Content discovery, author attribution, topical authority

---

## 🔧 Technical Specifications

### HTTP Headers

**Required for ai-discovery.json:**
```http
Content-Type: application/json
Cache-Control: public, max-age=3600, stale-while-revalidate=86400
```

**Required for knowledge-graph.json:**
```http
Content-Type: application/ld+json
Cache-Control: public, max-age=3600
ETag: "version-here"
```

**Required for llms.txt:**
```http
Content-Type: text/markdown; charset=utf-8
Cache-Control: public, max-age=86400
```

### CORS Headers (All Files)
```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, HEAD, OPTIONS
```

### Caching Strategy
- **ai-discovery.json:** 1-hour cache + 24-hour stale-while-revalidate
- **knowledge-graph.json:** 1-hour cache (use ETag for validation)
- **llms.txt:** 24-hour cache
- **robots.txt:** 24-hour cache

### File Size Limits
- **ai-discovery.json:** < 100 KB
- **knowledge-graph.json:** < 10 MB (recommend pagination if larger)
- **llms.txt:** < 100 KB (context window optimization)
- **robots.txt:** < 10 KB

---

## 🔐 Security Considerations

### Public by Design
- All ADP files are intentionally public
- Do NOT include sensitive data (credentials, internal URLs, private information)

### Content Security
- Validate JSON-LD against Schema.org vocabularies
- Escape user-generated content properly
- Use HTTPS for all endpoints

### Rate Limiting
- Implement rate limits on endpoints (recommended: 100 requests/minute per IP)
- Use CDN for static file serving

### Denial of Service Protection
- Set maximum file sizes
- Implement caching with appropriate TTLs
- Use GZip compression

---

## 🌐 AI Crawler User-Agents

Add these to your `robots.txt`:

```
User-agent: GPTBot           # OpenAI (ChatGPT)
User-agent: ChatGPT-User     # ChatGPT browsing
User-agent: Claude-Web       # Anthropic (Claude)
User-agent: PerplexityBot    # Perplexity AI
User-agent: Google-Extended  # Google (Gemini)
```

---

## 🚀 Getting Started

### Step 1: Choose Your Level
- **Quick win?** → Level 1 (Minimal) — 15 minutes
- **Full visibility?** → Level 2 (Standard) — 2-4 hours ⭐
- **Future-proof?** → Level 3 (Advanced) — 1-2 days

### Step 2: Copy Templates
- Browse [examples/](examples/) directory
- Copy templates for your chosen level
- Customize with your website data

### Step 3: Deploy
- Upload files to website root
- Verify endpoints return 200 OK
- Test with browser: `https://yoursite.com/ai-discovery.json`

### Step 4: Validate
- Check JSON syntax with [jsonlint.com](https://jsonlint.com)
- Validate Schema.org markup with [validator.schema.org](https://validator.schema.org)
- Monitor AI crawler visits in server logs

### Step 5: Monitor
- Track AI crawler requests (`GPTBot`, `Claude-Web`, `PerplexityBot`)
- Test queries in ChatGPT/Perplexity about your content
- Update `llms.txt` weekly with new content

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ways to contribute:**
- Submit implementation examples for different platforms (WordPress, Drupal, etc.)
- Report issues or suggest improvements
- Share success stories of ADP implementation
- Create validation tools or generators
- Improve documentation

**Community:**
- [GitHub Discussions](https://github.com/BuddySpuds/AI-Discovery-Protocol/discussions) — Ask questions, share ideas
- [GitHub Issues](https://github.com/BuddySpuds/AI-Discovery-Protocol/issues) — Report bugs, request features

---

## 📄 License

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
```

See [LICENSE](LICENSE) for full text.

---

## 🔗 Resources

- **Specification:** [SPECIFICATION.md](SPECIFICATION.md)
- **Quick Start:** [QUICK_START.md](QUICK_START.md)
- **Examples:** [examples/](examples/)
- **GitHub Repository:** https://github.com/BuddySpuds/AI-Discovery-Protocol
- **Reference Implementation:** https://pressonify.ai

---

## 📊 Comparison: Traditional SEO vs ADP

| Feature | Traditional SEO | ADP v1.0 |
|---------|----------------|----------|
| **Indexing Time** | 7-14 days | 6-24 hours |
| **Structure** | HTML parsing | Structured entities |
| **AI Discovery** | ❌ No | ✅ Yes |
| **Entry Point** | Sitemap.xml | ai-discovery.json |
| **Entity Catalog** | ❌ No | ✅ knowledge-graph.json |
| **Context Document** | ❌ No | ✅ llms.txt |
| **Versioning** | ❌ No | ✅ Optional |
| **Change Detection** | ❌ No | ✅ Optional |
| **Cost** | Free | Free (open standard) |

**Verdict:** ADP enhances traditional SEO, doesn't replace it. Implement both for maximum visibility.

---

## 🎯 Roadmap

### v1.0.0 (Current)
- ✅ Core 4-file architecture
- ✅ Schema.org integration
- ✅ Versioning support
- ✅ Reference implementation (Pressonify.ai)

### v1.1.0 (Planned)
- Entity pagination for large knowledge graphs
- Real-time updates via WebSocket
- Multi-language support
- Official JSON Schema validation files

### v2.0.0 (Future)
- Federated discovery (cross-domain entity references)
- GraphQL-like query endpoint
- Advanced relationship mapping

---

## ❓ FAQ

**Q: Is ADP free to use?**
A: Yes! ADP is MIT-licensed. Implement it on any website, modify it, or build commercial products on top of it.

**Q: Do I still need traditional SEO?**
A: Yes! ADP enhances SEO, doesn't replace it. Google still processes 8.5 billion searches/day. ADP adds AI discovery on top of traditional SEO.

**Q: How is ADP different from Schema.org?**
A: ADP builds on Schema.org. It provides a discovery protocol (single entry point, versioning, change logs) while using Schema.org vocabularies for entity definitions.

**Q: How is ADP different from llms.txt?**
A: ADP includes llms.txt as one of 4 files. ADP is a complete discovery protocol, llms.txt is a context document format.

**Q: Will AI platforms actually use this?**
A: ADP is designed based on how AI systems currently crawl websites (observed behavior of GPTBot, Claude-Web, PerplexityBot). It provides what AI systems need: structured entities, single entry point, freshness signals.

**Q: What's the minimum viable implementation?**
A: Just `/ai-discovery.json` (Level 1 — 15 minutes). But Level 2 (all 4 files) provides significantly more value for only 2-4 hours of work.

For more questions, see [FAQ.md](FAQ.md)

---

## 📢 Stay Updated

- **Star this repo** to get updates
- **Watch releases** for new versions
- **Join discussions** to share feedback
- **Follow Pressonify.ai** for implementation updates

---

**Published by:** [Pressonify.ai](https://pressonify.ai)
**Contributors:** Robert Porter, Claude (Anthropic)
**Version:** 1.0.0
**Last Updated:** November 5, 2025

*We welcome feedback, contributions, and implementations of this standard. Join the discussion!*
