# ADP Results: Real Citation Outcomes

**Last Updated:** January 2026
**Data Source:** Anonymized Pressonify.ai customer data
**Methodology:** Perplexity API citation scanning + crawler hit logging

---

## Executive Summary

These are **real results** from businesses using ADP v2.1 via [Pressonify.ai](https://pressonify.ai). No simulations. No projections. Actual citations discovered in AI search results.

| Metric | Result |
|--------|--------|
| **Average time to first AI citation** | 2.4 days |
| **Citation detection rate** | 100% (all published PRs cited) |
| **Most active AI platform** | Perplexity (67% of citations) |
| **Crawler visits per month** | 1,200+ across 11 AI systems |

---

## Case Studies (Anonymized)

### Case Study 1: B2B SaaS Company

**Industry:** Marketing Technology
**Content Type:** Product launch announcement
**ADP Implementation:** Full (20 endpoints)

| Metric | Before ADP | After ADP |
|--------|------------|-----------|
| AI crawler visits/month | 12 | 847 |
| Citations discovered | 0 | 36 |
| Time to first citation | Never | 18 hours |
| Platforms citing | 0 | 4 (Perplexity, ChatGPT, Claude, Gemini) |

**Key Finding:** The company's press release was cited by Perplexity within 18 hours of publication. The citation appeared in response to the query "best [category] tools 2026" — a high-intent commercial query.

---

### Case Study 2: E-commerce Brand

**Industry:** Consumer Products
**Content Type:** Funding announcement
**ADP Implementation:** Standard (6 endpoints)

| Metric | Before ADP | After ADP |
|--------|------------|-----------|
| AI crawler visits/month | 3 | 234 |
| Citations discovered | 0 | 12 |
| Time to first citation | Never | 3 days |
| Platforms citing | 0 | 2 (Perplexity, ChatGPT) |

**Key Finding:** Direct brand queries ("tell me about [company]") returned citations to the funding announcement within 72 hours. The AI response included accurate funding amount and investor names from the structured press release.

---

### Case Study 3: Healthcare Startup

**Industry:** Digital Health
**Content Type:** FDA approval announcement
**ADP Implementation:** Full + News Namespace

| Metric | Before ADP | After ADP |
|--------|------------|-----------|
| AI crawler visits/month | 8 | 1,100+ |
| Citations discovered | 0 | 48 |
| Time to first citation | Never | 6 hours |
| Platforms citing | 0 | 4 |

**Key Finding:** Healthcare content with proper Schema.org markup (MedicalDevice, Organization) achieved the fastest citation time in our dataset. The `/news/speakable.json` endpoint enabled voice assistant citations.

---

## Citation Detection Methodology

### How We Track Citations

1. **Wide-Net Query Strategy** — 8 query templates per company, prioritized by success rate
2. **Perplexity API Integration** — `sonar` model with `return_citations: true`
3. **Daily Automated Scans** — 8pm GMT cron job scanning all recent content
4. **Attribution Matching** — SHA-256 fingerprinting to match citations to source PRs

### Query Templates (Ranked by Success Rate)

| Priority | Template | Success Rate |
|----------|----------|--------------|
| 1 | `tell me about {company}` | 86% |
| 1 | `what is {company}` | 84% |
| 1 | `{company}` (direct) | 82% |
| 2 | `{company} announcement` | 43% |
| 2 | `{company} latest news` | 38% |
| 3 | `{company} press release` | 31% |
| 3 | `recent news about {company}` | 27% |

**Key Insight:** Direct brand queries outperform news-style queries by 2-3x. Optimize your content for "What is [Company]?" queries.

---

## Crawler Activity Data

### AI Crawlers Detected (30-Day Sample)

| Crawler | Organization | Hits | % of Total |
|---------|--------------|------|------------|
| GPTBot | OpenAI | 523 | 42% |
| ClaudeBot | Anthropic | 312 | 25% |
| PerplexityBot | Perplexity | 198 | 16% |
| Google-Extended | Google | 145 | 12% |
| Amazonbot | Amazon | 69 | 5% |

### Most Crawled Endpoints

| Endpoint | Hits | Purpose |
|----------|------|---------|
| `/llms.txt` | 487 | Primary context document |
| `/knowledge-graph.json` | 342 | Entity catalog |
| `/ai-discovery.json` | 256 | Meta-index |
| `/feed.json` | 189 | Content updates |
| `/news/llms.txt` | 134 | News-specific context |

**Key Insight:** `/llms.txt` receives 3x more crawler traffic than any other endpoint. This is your most important ADP file.

---

## Time-to-Citation Analysis

### Distribution (n=127 PRs)

| Time Range | % of PRs | Cumulative |
|------------|----------|------------|
| < 24 hours | 23% | 23% |
| 1-3 days | 45% | 68% |
| 3-7 days | 27% | 95% |
| 7-14 days | 5% | 100% |

**Median time to first citation: 2.4 days**

### Factors Affecting Citation Speed

| Factor | Impact |
|--------|--------|
| Full ADP implementation (20 endpoints) | -40% time |
| News namespace included | -25% time |
| Schema.org NewsArticle markup | -20% time |
| Speakable content | -15% time |
| IndexNow notification | -10% time |

---

## Platform Comparison

### Citation Distribution by AI Platform

```
Perplexity    ████████████████████████████████████  67%
ChatGPT       ██████████████████                    18%
Claude        ████████                               8%
Gemini        ██████                                 6%
Other         █                                      1%
```

### Why Perplexity Dominates

1. **Real-time web search** — Perplexity crawls content daily
2. **Citation transparency** — Shows sources in responses
3. **API access** — Enables programmatic citation detection
4. **News focus** — Optimized for current events and announcements

---

## ROI Framework

### Citation Value Estimation

| Traffic Source | Est. Value/Visit | Citation Equivalent |
|----------------|------------------|---------------------|
| Google Organic | $2.50 | 1 citation ≈ 50-200 visits |
| Paid Search | $5.00 | 1 citation ≈ 25-100 visits |
| AI Citation | $15.00+ | High-intent, pre-qualified |

**Why AI citations are worth more:**
- Users asking AI have **purchase intent** (not just browsing)
- AI pre-qualifies your business as relevant to their query
- No click required for brand awareness (AI reads your content aloud)
- Compounds over time (AI learns your content)

### Customer LTV Impact (Early Data)

| Acquisition Source | Avg. Deal Size | Close Rate |
|--------------------|----------------|------------|
| Google Organic | $2,400 | 12% |
| Paid Ads | $1,800 | 8% |
| AI Citation Referral | $4,200 | 24% |

*Note: Early data from 3 B2B customers tracking source attribution. Sample size limited.*

---

## Competitive Landscape

### PR Platform AI-Readiness (December 2025)

| Platform | /llms.txt | /.well-known/ai.json | Crawler Tracking | Citation Detection |
|----------|-----------|----------------------|------------------|-------------------|
| PR Newswire | 404 | 404 | No | No |
| PRWeb | 404 | 404 | No | No |
| BusinessWire | 404 | 404 | No | No |
| GlobeNewswire | 404 | 404 | No | No |
| **Pressonify** | **200** | **200** | **Yes** | **Yes** |

**Conclusion:** Major PR platforms have zero AI discoverability infrastructure. Content published through them is invisible to AI search.

---

## Get These Results

### Option 1: DIY Implementation

Implement ADP yourself using this open specification:
- [SPECIFICATION.md](SPECIFICATION.md) — Complete protocol spec
- [QUICK_START.md](QUICK_START.md) — Implementation guide
- [examples/](examples/) — Code templates

**Time investment:** 2-4 hours (Standard), 1-2 weeks (Enterprise with citation tracking)

### Option 2: Pressonify (Done-For-You)

Get ADP implementation + citation tracking + results like these:

🚀 **[Try Pressonify Free →](https://pressonify.ai/generate?free=1)**

**What you get:**
- Full 20-endpoint ADP implementation
- Automatic Schema.org markup
- Citation tracking dashboard
- Daily citation reports
- IndexNow instant indexing
- AI-optimized press releases in 60 seconds

**Pricing:** Starting at €49/PR | [View Plans →](https://pressonify.ai/pricing)

---

## Data Transparency

### How This Data Was Collected

1. **Crawler hits** — Server-side logging with user-agent identification
2. **Citations** — Perplexity API scans with `return_citations: true`
3. **Attribution** — URL matching + headline similarity scoring
4. **Anonymization** — Company names removed, industries generalized

### Limitations

- Citation detection limited to Perplexity (API access)
- ChatGPT/Claude/Gemini citations detected via manual spot-checks
- Sample size: 127 press releases, 14 companies, 6-month period
- Results may vary based on industry, content quality, and timing

### Updates

This page is updated monthly with fresh data. Last update: January 2026.

---

## Questions?

- **Technical:** [GitHub Issues](https://github.com/BuddySpuds/AI-Discovery-Protocol/issues)
- **Implementation help:** [ai-discovery@pressonify.ai](mailto:ai-discovery@pressonify.ai)
- **Enterprise inquiries:** [enterprise@pressonify.ai](mailto:enterprise@pressonify.ai)

---

*Results documented by [Pressonify.ai](https://pressonify.ai) — The closed-loop citation platform*

*Publish → Index → Cite → Detect*
