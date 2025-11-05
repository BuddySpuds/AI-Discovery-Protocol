# Changelog

All notable changes to the AI Discovery Protocol will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
