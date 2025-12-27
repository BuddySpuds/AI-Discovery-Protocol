# Changelog

All notable changes to the AI Discovery Protocol will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2.1] - 2025-12-27

### Added
- **Proof Infrastructure** — New component for verifying AI crawler engagement
  - **Crawler Hit Tracking** — Log and analyze AI crawler activity on ADP endpoints
    - Identifies 11 AI crawlers: GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Bingbot, Cohere-AI, YouBot, Applebot-Extended, Meta-ExternalAgent, CCBot, Diffbot
    - Fire-and-forget async logging (zero performance impact)
    - Daily aggregation for trend analysis
  - **Citation Monitoring** — Track when AI platforms cite your content
    - Perplexity API integration with `sonar` model
    - Multi-platform support (ChatGPT, Claude, Gemini passive tracking)
    - Query deduplication via SHA-256 hashing (24-hour window)
  - **Public Transparency API** — Expose crawler statistics
    - `/api/v1/adp/stats` — Overall statistics
    - `/api/v1/adp/stats/crawlers` — Top crawlers ranked
    - `/api/v1/adp/stats/endpoints` — Top endpoints ranked
    - `/api/v1/adp/stats/daily` — Daily trends

- **Enhanced HTTP Headers** — Additional response headers for ADP endpoints
  - `Content-Digest: sha-256=...` — Integrity verification
  - `X-Update-Frequency` — Crawler scheduling hints (realtime, hourly, daily, weekly)
  - Complements existing `ETag` for cache validation

- **llms-lite.txt Endpoint** — Minimal context document (198 tokens)
  - For systems with strict context limits
  - Complements `/llms.txt` (1,247 tokens) and `/llms-full.txt` (13,451 tokens)

- **CORS Support** — `Access-Control-Allow-Origin: *` on all ADP endpoints
  - Enables client-side AI tools to fetch ADP resources
  - Required for browser-based AI assistants

### Changed
- **Version format** — Incremented to 2.1 (proof infrastructure release)
- **Documentation** — Added proof infrastructure implementation guide
- **Reference implementation** — Pressonify.ai upgraded to ADP v2.1+

### Proof Infrastructure Philosophy
The gap between "claiming AI optimization" and "proving AI engagement" undermines trust in the ADP ecosystem. v2.1 addresses this with:

1. **Transparency** — Public APIs showing crawler activity
2. **Verification** — Citation tracking confirms AI systems use your content
3. **Accountability** — Logged evidence replacing marketing claims

### Reference Implementation
- **Pressonify.ai** upgraded to ADP v2.1+ on December 27, 2025
- **Live endpoints:**
  - Crawler stats: https://pressonify.ai/api/v1/adp/stats
  - Citation stats: https://pressonify.ai/api/v1/citations/stats
  - LLM context: https://pressonify.ai/llms.txt
- **Documentation:** [ADP 2.1+: Proof Infrastructure](https://pressonify.ai/blog/adp-2-1-proof-infrastructure-crawler-tracking)

### Industry Comparison (December 2025)
| Platform | /llms.txt | /.well-known/ai.json | Crawler Tracking |
|----------|-----------|----------------------|------------------|
| PR Newswire | 404 | 404 | No |
| PRWeb | 404 | 404 | No |
| BusinessWire | 404 | 404 | No |
| GlobeNewswire | 404 | 404 | No |
| **Pressonify** | **200** | **200** | **Yes (11 crawlers)** |

Full comparison: [PR Platforms AI-Readiness Audit](https://pressonify.ai/blog/pr-platforms-ai-readiness-comparison-2025)

---

## [2.0] - 2025-12-02

### Added
- **`capabilities` object** — New top-level object declaring protocol feature support
  - `supportsVersioning` — Boolean flag for versioning support
  - `supportsIncrementalUpdates` — Boolean flag for incremental update support
  - `supportsChangeDetection` — Boolean flag for change detection capability
  - `updateFrequency` — Enum declaring content update frequency (realtime, hourly, daily, weekly, monthly, quarterly, annually)
- **`contact` object** — New top-level object for ADP support channels
  - `email` — Email address for ADP-related inquiries
  - `issuesUrl` — URL for reporting issues with ADP implementation
- **`shopify.optimization` block** — Enhanced Shopify optimization metadata (v2.0 feature)
  - `version` — Optimization scoring model version
  - `scoringModel` — Name of scoring algorithm (e.g., "adp-v2.0-8factor")
  - `distribution` — Distribution of entities by optimization level
    - `fullyOptimized` — Count of entities with SEO score >= 70
    - `partiallyOptimized` — Count of entities with SEO score 45-69
    - `basic` — Count of entities with SEO score < 45
  - `baselineScoreRange` — Dynamic baseline score range [min, max] for optimization
  - `averageScore` — Average SEO score across all optimized entities
  - `lastOptimized` — ISO 8601 timestamp of last optimization run

### Changed
- **Version pattern simplified** — Changed from semantic versioning (1.0.0) to major.minor format (2.0)
  - Pattern updated from `^\d+\.\d+\.\d+$` to `^\d+\.\d+$`
  - More intuitive for protocol versions (spec versions, not implementation versions)
  - Reduces version number churn for minor spec clarifications
- **`metadata` object** — Changed from required to optional in v2.0 schema
  - `language` and `updateFrequency` no longer required
  - `updateFrequency` moved to `capabilities` object (more semantically appropriate)
- **Optimization transparency** — 8-factor scoring model now exposed via `scoringModel` field
  - Enables AI systems to understand optimization methodology
  - Supports multiple scoring algorithms in the future
  - Provides confidence in optimization quality metrics

### Deprecated
- **`shopify.optimizationStatus`** — Replaced by more comprehensive `shopify.optimization` block
  - Still supported in v2.0 for backward compatibility
  - Will be removed in v3.0
  - Migration: Use `shopify.optimization.distribution` instead

### Reference Implementation
- **Pressonify.ai** upgraded to ADP v2.0 on December 2, 2025
- Live v2.0 endpoint: https://pressonify.ai/ai-discovery.json
- Full example: [examples/v2/ai-discovery.json](examples/v2/ai-discovery.json)
- Optimization distribution: 342 fully optimized, 89 partially optimized, 10 basic entities
- Average optimization score: 73.5/100 (dynamic baseline: 35-55)

### Migration Notes
- **v1.0 files remain valid** — v2.0 is backward compatible
- **Version field update required** — Change from "1.0.0" to "2.0" format
- **Optional enhancements** — New `capabilities` and `contact` objects are optional
- **Shopify users** — Consider migrating from `optimizationStatus` to `optimization`
- **Full migration guide**: [docs/V2_MIGRATION_GUIDE.md](docs/V2_MIGRATION_GUIDE.md)

---

## [1.0.0] - 2025-11-05

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

## [Unreleased]

### Planned for v1.1.0
- Entity pagination for large knowledge graphs (>10,000 entities)
- Real-time updates via WebSocket endpoint
- Multi-language support and localization
- Official JSON Schema validation files
- Validation tools (Python, JavaScript, CLI)
- Additional platform implementations (WordPress, Drupal, Shopify)

### Under Consideration for v2.0.0
- Federated discovery (cross-domain entity references)
- GraphQL-like query endpoint
- Advanced relationship mapping beyond Schema.org
- Real-time change feeds
- Subscription model for updates

---

## Release Notes

### v1.0.0 Highlights

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

[1.0.0]: https://github.com/BuddySpuds/AI-Discovery-Protocol/releases/tag/v1.0.0
