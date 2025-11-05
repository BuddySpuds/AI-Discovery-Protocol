# AI Discovery Protocol: Design Decisions & Rationale

**Document Version:** 1.0
**Date:** November 2, 2025
**Author:** Robert Porter (with Claude, Anthropic)

---

## Executive Summary

This document explains the **architectural decisions** behind the AI Discovery Protocol (ADP) v1.0, including features we **intentionally excluded** to maximize adoption potential.

**TL;DR:** We prioritized **simplicity and adoption** over feature richness, learning from successful standards (robots.txt, RSS, sitemap.xml) that gained universal adoption through minimal friction.

---

## Design Philosophy: The Simplicity Paradox

### Research-Backed Insight

**Successful web standards (widely adopted):**
- **robots.txt** (1994): 3 directives, plain text → 30-year universal adoption
- **sitemap.xml** (2005): Simple XML, Google/Yahoo/MS backing → De facto standard
- **RSS** (1999): Straightforward feed format → Billions of feeds

**Failed/struggling standards (complex but powerful):**
- **WCAG 2.1**: 95.9% non-compliance (too complex)
- **llms.txt** (2024): Major AI platforms DON'T support it yet
- **Semantic Web/RDF**: Never achieved mass adoption (too complex)

### Critical Factor: Implementation Friction

The #1 predictor of standard adoption is **how easy it is to implement**, not how powerful it is.

**Formula:**
```
Adoption Rate ∝ (Value Provided) / (Implementation Friction)²
```

Implementation friction compounds exponentially, not linearly.

---

## Enhancement Analysis: What We Included vs Excluded

### ❌ EXCLUDED: Enhancement 1 - ai-discovery.xml

**Original Proposal:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ai-discovery xmlns="http://yoursite.com/schemas/ai-discovery">
  <metadata>
    <version>2.0</version>
    <endpoints>
      <endpoint type="knowledge-graph" format="json-ld">
        <url>https://site.com/knowledge-graph.json</url>
        <priority>1.0</priority>
      </endpoint>
    </endpoints>
  </metadata>
</ai-discovery>
```

**Why Excluded:**

1. **Format Confusion**: XML vs JSON — developers would ask "which one do I use?"
2. **Redundancy**: Duplicates `ai-discovery.json` (Enhancement 4)
3. **Extra Maintenance**: Another file to keep updated
4. **Declining Format**: XML is legacy; JSON is the modern standard
5. **Adoption Friction**: Adds implementation complexity without sufficient value

**Decision:** Skip entirely. JSON is the future.

---

### ✅ INCLUDED: Enhancement 2 - Versioning & Change Detection

**Included Features:**

```json
{
  "@type": "KnowledgeGraph",
  "version": "2.7.1",
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
      }
    ]
  }
}
```

**Why Included:**

1. **High Value**: Enables incremental crawling (massive efficiency gain)
2. **Low Friction**: Just adds metadata to existing JSON structure
3. **Modern Pattern**: GraphQL, REST APIs already do this
4. **Practical Benefit**: AI systems can detect changes without full re-crawls
5. **Optional**: Sites can omit `changeLog` and still comply

**Value/Friction Ratio:** ⭐⭐⭐⭐⭐ (Very High)

---

### ⚠️ PARTIAL: Enhancement 3 - AI-Specific HTTP Headers

**Original Proposal:**
```http
X-LLM-Optimized: true
X-Schema-Version: 2.1
X-Entity-Count: 132
X-Knowledge-Graph-Version: 2.1.5
X-Last-Updated: 2025-11-01T12:00:00Z
X-AI-Crawl-Priority: high
X-Supports-Incremental-Updates: true
```

**What We Kept:**
```http
Content-Type: application/ld+json
Cache-Control: public, max-age=3600, stale-while-revalidate=86400
Last-Modified: Sat, 02 Nov 2025 11:30:00 GMT
ETag: "2.7.1"
```

**Why Partial Implementation:**

**Custom `X-` Headers (Excluded):**
1. **Deprecated Standard**: RFC 6648 discourages `X-` prefix headers
2. **HTTP/2 Overhead**: Headers add latency
3. **Redundancy**: Information already in JSON body
4. **Server Configuration**: Requires backend changes (friction)

**Standard HTTP Headers (Included):**
1. **Already Implemented**: Most servers send these automatically
2. **Cache Control**: Essential for CDN/browser caching
3. **Last-Modified/ETag**: Standard cache invalidation
4. **Zero Friction**: No custom configuration required

**Decision:** Use standard HTTP headers only. Skip custom `X-` headers.

---

### ✅✅✅ INCLUDED: Enhancement 4 - ai-discovery.json Meta-Index

**Included (Core Innovation):**

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
      "entityCount": 132,
      "version": "2.7.1"
    },
    "contextDocument": {
      "url": "https://example.com/llms.txt",
      "format": "text/markdown"
    }
  },
  "capabilities": {
    "supportsVersioning": true,
    "supportsIncrementalUpdates": true
  }
}
```

**Why Included (MUST-HAVE):**

1. **Single Entry Point**: AI systems hit ONE file first
2. **Discoverability**: Maps entire AI discovery ecosystem
3. **Extensibility**: Easy to add new endpoints in the future
4. **Simplicity**: JSON format, modern, developer-friendly
5. **Backwards Compatible**: Doesn't break existing files
6. **Zero Ambiguity**: Clear contract for what's available

**Value/Friction Ratio:** ⭐⭐⭐⭐⭐⭐ (Exceptional)

**This is the killer feature** that differentiates ADP from scattered Schema.org markup.

---

## Architectural Decisions

### Decision 1: Four Files, Not Seven

**Options Considered:**

**Option A: Minimalist (2 files)**
- `ai-discovery.json` + `knowledge-graph.json`
- ❌ No human-readable context
- ❌ Ignores existing `robots.txt` standard

**Option B: Maximal (7+ files)**
- `ai-discovery.json` + `ai-discovery.xml` + `knowledge-graph.json` + `knowledge-graph.xml` + `llms.txt` + `llms.md` + `robots.txt`
- ❌ Too complex
- ❌ Format confusion

**Option C: Balanced (4 files)** ✅ **CHOSEN**
- `ai-discovery.json` (meta-index)
- `knowledge-graph.json` (structured entities)
- `llms.txt` (human-readable context)
- `robots.txt` (standard crawler directives)

**Rationale:**
- **Familiar patterns**: Builds on robots.txt/sitemap.xml success
- **Progressive enhancement**: Sites can implement piece by piece
- **Clear separation of concerns**: Each file has distinct purpose
- **Modern tooling**: JSON parsers are universal

---

### Decision 2: JSON-LD, Not RDF/XML

**Why JSON-LD:**
1. **Developer familiarity**: Every developer knows JSON
2. **Schema.org compatibility**: W3C-recommended format
3. **Tooling ecosystem**: Libraries exist in every language
4. **Human-readable**: Developers can edit without specialized tools

**Why NOT RDF/XML:**
1. **Legacy format**: XML is declining
2. **Complexity**: Triple stores, SPARQL queries
3. **Poor adoption**: Semantic Web never achieved mainstream use
4. **High friction**: Requires specialized knowledge

**Decision:** JSON-LD exclusively. No XML variants.

---

### Decision 3: Progressive Enhancement (3 Levels)

**Level 1: Minimal** (15 minutes)
- `ai-discovery.json` only
- Signals AI-friendly intent
- **Value:** Basic discoverability
- **Friction:** Near-zero

**Level 2: Standard** (2-4 hours)
- + `knowledge-graph.json`
- + `llms.txt`
- **Value:** Full AI discoverability
- **Friction:** Low (copy/paste templates)

**Level 3: Advanced** (1-2 days)
- + Versioning
- + Change logs
- + Custom endpoints
- **Value:** Incremental crawling support
- **Friction:** Medium (requires backend logic)

**Rationale:**
- **No all-or-nothing**: Sites can start small
- **Incremental value**: Each level adds benefit
- **Adoption funnel**: Easy entry, gradual sophistication

---

### Decision 4: Semantic Versioning

**Format:** `MAJOR.MINOR.PATCH` (e.g., `2.7.1`)

**Versioning applies to:**
1. **Specification itself**: `ai-discovery.json` format version
2. **Knowledge graph content**: `knowledge-graph.json` data version

**Why Semantic Versioning:**
1. **Universal standard**: NPM, Maven, PyPI use it
2. **Clear breaking changes**: MAJOR version bump signals incompatibility
3. **Tooling support**: Automated dependency management
4. **Developer familiarity**: Everyone knows semver

**Alternative Considered:** SchemaVer (MODEL-REVISION-ADDITION)
- ❌ Less familiar to developers
- ❌ Overkill for this use case

---

### Decision 5: Change Log Format

**Chosen Format:**
```json
"changes": [
  {
    "timestamp": "2025-11-02T11:30:00Z",
    "entityType": "Product",
    "entityId": "https://example.com/products/widget-pro",
    "changeType": "updated",
    "modifiedFields": ["price", "availability"]
  }
]
```

**Change Types:**
- `created`: New entity added
- `updated`: Existing entity modified
- `deleted`: Entity removed (tombstone)

**Why This Format:**
1. **Granular**: Field-level change tracking
2. **Queryable**: AI systems can filter by `entityType`
3. **Temporal**: Sorted by `timestamp`
4. **Actionable**: AI knows exactly what changed

**Alternative Considered:** Git-style diffs
- ❌ Too complex for most implementations
- ❌ Requires diff parsing libraries

---

## Standard HTTP Headers Strategy

### What We Recommend

**Required:**
```http
Content-Type: application/json
```

**Strongly Recommended:**
```http
Cache-Control: public, max-age=3600, stale-while-revalidate=86400
Last-Modified: Sat, 02 Nov 2025 11:30:00 GMT
```

**Optional:**
```http
ETag: "2.7.1"
Vary: Accept-Encoding
```

**Why:**
- **Standard headers**: Every HTTP server supports these
- **Cache optimization**: CDN-friendly
- **Conditional requests**: AI systems can use `If-Modified-Since`
- **Zero friction**: Most frameworks set these automatically

---

## Security Decisions

### Public by Design

**Decision:** All ADP files are **publicly accessible** (like robots.txt).

**Rationale:**
1. **Transparency**: AI systems need open access
2. **No authentication**: Eliminates complexity
3. **Follows precedent**: robots.txt, sitemap.xml are public

**Guidance:**
- ❌ Don't include sensitive data (API keys, credentials)
- ❌ Don't expose internal URLs
- ✅ Rate limit endpoints (prevent abuse)
- ✅ Use HTTPS (prevent tampering)

---

### Rate Limiting

**Recommended:**
```
- 60 requests/minute per IP (ai-discovery.json)
- 10 requests/minute per IP (knowledge-graph.json)
```

**Rationale:**
- Prevent DOS attacks
- Allow legitimate crawlers
- Protect server resources

---

## Naming Decisions

### Why "AI Discovery Protocol" (Not "Triumvirate")?

**Options Considered:**

1. **Triumvirate System** → Too obscure, implies exactly 3 components
2. **AI Entity Protocol** → Too narrow (not just entities)
3. **AI Discovery Protocol** → ✅ **CHOSEN**

**Rationale:**
- **Clear purpose**: "Discovery" explains what it does
- **Extensible**: Can add more components beyond original 3
- **Professional**: "Protocol" signals seriousness
- **Memorable**: Short acronym (ADP)

---

### File Naming Conventions

**Chosen:**
- `ai-discovery.json` (lowercase, hyphenated)
- `knowledge-graph.json` (lowercase, hyphenated)
- `llms.txt` (lowercase, established convention)

**Why Lowercase:**
1. **Web convention**: URLs are case-sensitive on Linux
2. **Avoid errors**: `AI-Discovery.json` vs `ai-discovery.json` confusion
3. **Consistency**: Matches robots.txt, sitemap.xml, favicon.ico

**Why Hyphenation:**
1. **Readability**: `ai-discovery` vs `aidiscovery`
2. **SEO-friendly**: Hyphens are URL-safe
3. **Convention**: Follows web standards (open-graph, etc.)

---

## Lessons from llms.txt

### What llms.txt Got Right

1. ✅ **Simplicity**: Plain text, easy to create
2. ✅ **Human-readable**: Markdown format
3. ✅ **Low friction**: Copy/paste template
4. ✅ **Open standard**: MIT License

### What llms.txt Missed

1. ❌ **No structured data**: Can't query entities programmatically
2. ❌ **No versioning**: AI systems can't detect changes
3. ❌ **No discovery mechanism**: How do AI systems know it exists?
4. ❌ **Platform support**: Major AI providers don't use it (yet)

### How ADP Addresses These

1. ✅ **Structured catalog**: `knowledge-graph.json` with Schema.org entities
2. ✅ **Versioning**: Semantic versions + change logs
3. ✅ **Entry point**: `ai-discovery.json` maps all resources
4. ✅ **Includes llms.txt**: We're complementary, not competitive

---

## Future-Proofing Decisions

### Extensibility Mechanisms

**1. Custom Endpoints**
```json
"endpoints": {
  "knowledgeGraph": { ... },
  "customAPI": {
    "url": "https://example.com/custom-api",
    "description": "Custom entity query API",
    "docs": "https://example.com/api-docs"
  }
}
```

**2. Capability Flags**
```json
"capabilities": {
  "supportsVersioning": true,
  "supportsGraphQL": true,
  "supportsRealtime": false
}
```

**3. Namespace Versioning**
```json
"$schema": "https://pressonify.ai/schemas/ai-discovery/v1.0.json"
```

**Rationale:**
- **Forward compatibility**: New features don't break old parsers
- **Gradual adoption**: Sites can opt into new capabilities
- **Innovation space**: Community can experiment

---

## Adoption Strategy Decisions

### Why MIT License

**Options Considered:**
1. **Patent + Licensing** → High revenue potential, blocks adoption
2. **GPL** → Viral license, deters commercial use
3. **Apache 2.0** → Patent grant, but more complex
4. **MIT** → ✅ **CHOSEN**

**Rationale:**
- **Maximum adoption**: Fewest restrictions
- **Commercial-friendly**: Companies can use freely
- **Precedent**: robots.txt, RSS use permissive licenses
- **Network effects**: More adoption = more value

---

### Why Open Source First

**Strategy:**
1. **Release standard** (MIT License)
2. **Build tooling** (MCP server, plugins)
3. **Monetize implementation**, not specification

**Historical Precedents:**
- **Red Hat**: Open-source Linux → $34B acquisition (IBM)
- **MongoDB**: Open-source database → $26B valuation
- **Elastic**: Open-source search → $10B valuation

**Expected Outcome:**
- **Year 1**: 100-500 implementations
- **Year 2**: 5,000-10,000 implementations
- **Year 3**: Industry standard status

---

## Trade-Offs & Compromises

### Compromise 1: No Real-Time Updates (v1.0)

**Considered:** WebSocket endpoint for live entity updates

**Excluded Because:**
- ❌ High implementation complexity
- ❌ Server resource intensive
- ❌ Overkill for most use cases

**Deferred to:** v2.0 (Future Extensions)

---

### Compromise 2: No Entity Pagination (v1.0)

**Considered:** Paginated knowledge graphs for sites with 10,000+ entities

**Excluded Because:**
- ❌ Adds complexity to parsers
- ❌ Most sites have <1,000 entities
- ❌ Can be solved with file splitting

**Deferred to:** v1.1 (Planned Features)

---

### Compromise 3: No GraphQL Endpoint (v1.0)

**Considered:** GraphQL API for entity queries

**Excluded Because:**
- ❌ High implementation barrier
- ❌ Requires backend infrastructure
- ❌ Not necessary for basic discovery

**Deferred to:** v2.0 (Potential Extensions)

---

## Success Metrics

### Adoption Indicators

**Phase 1 (Months 1-3):**
- 100+ implementations
- HackerNews/Reddit discussions
- GitHub stars > 500

**Phase 2 (Months 4-6):**
- WordPress plugin: 1,000+ active installs
- Shopify app adoption
- Conference talks accepted

**Phase 3 (Months 7-12):**
- AI platform adoption (OpenAI, Anthropic, Google)
- W3C Community Group formed
- 5,000+ implementations

**Phase 4 (Year 2+):**
- IETF RFC submission
- Schema.org vocabulary extension
- Industry standard status

---

## Lessons Learned

### 1. Simplicity Compounds

Every additional feature reduces adoption exponentially. We excluded:
- XML variants (format confusion)
- Custom HTTP headers (implementation friction)
- Real-time updates (complexity)
- GraphQL endpoints (high barrier)

**Result:** 4-file architecture that's easy to understand and implement.

---

### 2. Standards Need a "Why"

**llms.txt struggled because:** AI platforms don't support it yet

**ADP's advantage:** Solves a **clear pain point**:
- AI systems waste time crawling 100 HTML pages
- No standard way to discover structured entities
- No incremental update mechanism

**Lesson:** Standards need compelling value proposition.

---

### 3. Build for Developers, Not Academics

**Failed standards (Semantic Web, RDF):** Designed by researchers, too complex for developers

**Successful standards (REST, JSON, Markdown):** Designed by practitioners, easy to use

**ADP's approach:**
- JSON (not XML)
- Schema.org (not custom ontologies)
- Progressive enhancement (not all-or-nothing)
- Code examples (not just specifications)

---

### 4. Open Source ≠ Free Labor

**Misconception:** Open source means giving away value

**Reality:** Open standards create **ecosystem value**

**Our model:**
- Standard (free) → Drives adoption
- Tooling (paid) → Captures value
- Consulting (premium) → High margins

**Precedent:** Red Hat, MongoDB, Elastic (billions in value from open-source foundations)

---

## Conclusion

The AI Discovery Protocol v1.0 represents a **carefully balanced** design that prioritizes:

1. **Adoption** over feature richness
2. **Simplicity** over theoretical perfection
3. **Developer experience** over academic purity
4. **Extensibility** over completeness

By learning from successful standards (robots.txt, RSS, sitemap.xml) and avoiding the pitfalls of failed ones (Semantic Web, WCAG complexity), we've created a standard with genuine adoption potential.

**The test:** Will developers implement this in 15 minutes without reading documentation?

**Our answer:** Yes, because we designed for them, not for us.

---

## References

### Standards Research
- **robots.txt History**: 30 years of voluntary compliance → IETF RFC 9309 (2022)
- **sitemap.xml Adoption**: Proposed 2005, Google/Yahoo/MS backing → De facto standard
- **llms.txt Status**: Proposed Sept 2024, 70+ early adopters, major platforms not yet supporting

### Adoption Studies
- **WCAG 2.1 Compliance**: 95.9% failure rate (2024) due to complexity
- **Schema.org Adoption**: ~40% of websites (success through simplicity)
- **Semantic Web/RDF**: <1% adoption (failure due to complexity)

### Technical Resources
- **JSON-LD 1.1 W3C Recommendation**: https://www.w3.org/TR/json-ld11/
- **Schema.org Specification**: https://schema.org/docs/schemas.html
- **RFC 3339 (Date/Time)**: https://www.rfc-editor.org/rfc/rfc3339

---

**Document Prepared By:** Robert Porter (Pressonify.ai)
**Contributors:** Claude (Anthropic)
**Last Updated:** November 2, 2025
**License:** MIT License
