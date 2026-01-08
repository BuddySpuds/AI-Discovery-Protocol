# Changelog

All notable changes to the AI Discovery Protocol will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.1] - 2026-01-08

### News AI Discoverability Sprint

Major expansion from 11 to 20 endpoints with new capabilities for news publishers and proof infrastructure.

### Added

**News Namespace (`/news/*`)**
- `/news/llms.txt` - News-specific AI context document
- `/news/speakable.json` - Voice assistant-optimized content (Schema.org Speakable)
- `/news/changelog.json` - Platform version history tracking
- `/news/archive.jsonl` - Historical content in JSONL streaming format

**New Endpoints**
- `/opensearch.xml` - Browser search plugin integration
- `/api/webhooks/discovery` - Webhook registration endpoint
- `/llms-lite.txt` - Minimal context (~200 bytes)
- `/llms-full.txt` - Comprehensive context (50KB+)

**Proof Infrastructure**
- AI crawler hit logging (GPTBot, ClaudeBot, PerplexityBot, etc.)
- Citation detection via Perplexity API
- ROI attribution (citations → source content)
- Public stats API (`/api/v1/adp/stats`)
- Daily citation reports with wide-net query strategy

**Documentation**
- `docs/NEWS_NAMESPACE.md` - News publisher implementation guide
- `docs/PROOF_INFRASTRUCTURE.md` - Citation tracking documentation

### Changed

- Endpoint count: 11 → 20
- Implementation levels: 3 → 4 (added Enterprise tier with citation tracking)
- Reference implementation updated to Pressonify.ai v2.9.6

---

## [2.0] - 2025-12-08

### HTTP Security & Capabilities

Enhanced protocol with HTTP headers and capabilities declaration.

### Added

**HTTP Security Headers**
- `ETag` - Cache validation
- `Content-Digest: sha-256=...` - Integrity verification
- `X-Update-Frequency` - Crawler scheduling hints (daily/weekly/monthly)
- `Access-Control-Allow-Origin: *` - CORS support for AI tools

**Capabilities Object**
```json
"capabilities": {
  "supportsVersioning": true,
  "supportsIncrementalUpdates": true,
  "supportsChangeDetection": true,
  "updateFrequency": "daily"
}
```

**Contact Object**
```json
"contact": {
  "email": "ai-support@example.com",
  "issuesUrl": "https://github.com/example/issues"
}
```

**New Endpoints**
- `/.well-known/ai.json` - Standardized well-known location
- `/feed.json` - JSON Feed v1.1 format
- `/updates.json` - Recent content changes
- `/ai-sitemap.xml` - AI-optimized sitemap
- `/ai-discovery.md` - Human-readable discovery doc

### Changed

- Version format: `1.0.0` → `2.0` (simplified major.minor)
- Endpoint count: 4 → 11
- CORS enabled on all endpoints by default

---

## [1.0.0] - 2025-11-05

### Initial Release

First public release of the AI Discovery Protocol specification.

### Added
- **Initial specification release** — Complete technical specification (13,500 words)
- **Core 4-file architecture:**
  - `/ai-discovery.json` — Meta-index (single entry point)
  - `/knowledge-graph.json` — Schema.org entity catalog
  - `/llms.txt` — Human-readable context document
  - `/robots.txt` — AI crawler directives
- **Three implementation levels:**
  - Level 1 (Minimal) — 15 minutes
  - Level 2 (Standard) — 2-4 hours (RECOMMENDED)
  - Level 3 (Advanced) — 1-2 days
- **Comprehensive documentation:**
  - SPECIFICATION.md — Full technical spec
  - QUICK_START.md — Implementation guides
  - DESIGN_DECISIONS.md — Design rationale
  - docs/EXPLAINED_SIMPLY.md — Layperson explanation
  - docs/COMPARISON.md — Comparison to other standards
  - README.md — Complete technical guide with examples
  - FAQ.md — Frequently asked questions
- **Working examples:**
  - examples/minimal/ — Level 1 implementation
  - examples/standard/ — Level 2 implementation (generic templates)
  - examples/advanced/ — Level 3 with versioning and change logs
  - examples/press-release-platform/ — Pressonify.ai reference implementation
- **Reference implementation:**
  - Pressonify.ai as first platform with full ADP v1.0 compliance
  - Live endpoints: ai-discovery.json, knowledge-graph.json, llms.txt, robots.txt
  - Validation report documenting 100% compliance
- **Security guidelines:**
  - Public-by-design considerations
  - CORS configuration
  - Rate limiting recommendations
  - Content security best practices
- **MIT License** — Open source, free to use and modify

### Reference Implementation
- **Pressonify.ai** achieved full ADP v1.0 compliance on November 2, 2025
- Performance metrics: 0.592s average load time, 68% compression ratio
- 17 entities in knowledge graph (4 base + 13 NewsArticle entities)
- Dynamic updates: Press releases added to knowledge graph within seconds

### Contributors
- Robert Porter (Pressonify.ai)
- Claude (Anthropic) — Specification development assistance

---

## Version Comparison

| Feature | v1.0 | v2.0 | v2.1 |
|---------|------|------|------|
| Endpoints | 4 | 11 | 20 |
| News Namespace | - | - | ✓ |
| HTTP Headers | - | ✓ | ✓ |
| Proof Infrastructure | - | - | ✓ |
| Capabilities Object | - | ✓ | ✓ |
| CORS Support | - | ✓ | ✓ |
| Tiered Content | - | - | ✓ |
| Voice Optimization | - | - | ✓ |
| Citation Tracking | - | - | ✓ |

---

## Migration Notes

### v1.0 → v2.0

1. Update version in `ai-discovery.json`:
   ```json
   "version": "2.0"
   ```

2. Add capabilities object

3. Add HTTP headers to all endpoints

4. (Optional) Add new endpoints: `/.well-known/ai.json`, `/feed.json`

### v2.0 → v2.1

1. Update version:
   ```json
   "version": "2.1"
   ```

2. (Optional) Add news namespace if publishing news content

3. (Optional) Implement proof infrastructure for ROI tracking

4. (Optional) Add tiered content (`/llms-lite.txt`, `/llms-full.txt`)

---

## Release Notes

### v2.1 Highlights

**Why v2.1?**
- Prove ADP effectiveness with crawler tracking and citation detection
- Voice assistant optimization for smart speakers
- News-specific content for publishers
- Historical archives in efficient streaming format

**Key Benefits:**
- **Measurable ROI:** Track AI crawler visits and citations
- **Voice-ready:** Speakable content for Alexa, Google Assistant, Siri
- **News optimized:** Dedicated namespace for time-sensitive content
- **Streaming archives:** Efficient JSONL format for large datasets

### v1.0 Highlights

**Why ADP?**
Traditional SEO was designed for keyword-based crawlers. AI systems (ChatGPT, Claude, Perplexity, Gemini) need structured entity catalogs, freshness signals, and context-optimized documents. ADP provides a standard discovery protocol for the AI era.

**Key Benefits:**
- **10x faster discovery:** AI systems find content in 6-24 hours vs 7-14 days
- **Structured understanding:** Entity catalogs instead of HTML parsing
- **Future-proof:** Designed for AI reasoning systems
- **Open standard:** MIT-licensed, free to implement

**Who Should Use This?**
- E-commerce sites (product discovery by AI shopping assistants)
- SaaS companies (brand awareness, feature documentation)
- Publishers (content discovery, author attribution)
- Any website wanting visibility in AI search results

**Getting Started:**
See [QUICK_START.md](QUICK_START.md) for implementation guides.

---

[2.1]: https://github.com/BuddySpuds/AI-Discovery-Protocol/releases/tag/v2.1
[2.0]: https://github.com/BuddySpuds/AI-Discovery-Protocol/releases/tag/v2.0
[1.0.0]: https://github.com/BuddySpuds/AI-Discovery-Protocol/releases/tag/v1.0.0
