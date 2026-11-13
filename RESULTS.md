# What AI crawlers read: measured results

**Updated:** 13 November 2026
**Source:** request logs of [pressonify.ai](https://pressonify.ai), the reference implementation
**Window:** 14 October to 12 November 2026 (30 days, UTC)
**Sample:** 22,168 requests from 18 crawlers, identified by user agent

This page reports what one site measured. It is one site, so read it as a
case, not as a law. It is published because first-party logs of which crawlers
read which discovery files are hard to find, and the protocol should follow
them.

---

## Summary

| What was requested | Requests | Share | Crawlers |
|---|---:|---:|---:|
| HTML pages (articles, releases, hubs, everything else) | 15,532 | 70.1% | 18 |
| Markdown copies of pages | 5,290 | 23.9% | 13 |
| `robots.txt` and sitemaps | 1,019 | 4.6% | 12 |
| Root discovery files (context files, feeds, news files, manifests) | 327 | 1.5% | 13 |

Three things follow.

1. **Crawlers read pages.** Seven requests in ten were for ordinary HTML.
2. **Markdown copies of pages are read. Root discovery files mostly are not.**
   The copies drew sixteen times the requests of every root file combined.
3. **The meta-index is not used as an entry point.** `/ai-discovery.json` was
   requested 30 times by four crawlers. Nothing in the logs suggests a crawler
   fetches it first and then follows it.

These findings are the reason ADP 3.1 makes page copies Level 1 and moves the
root files to optional levels. See [SPECIFICATION.md](SPECIFICATION.md).

---

## Root discovery files, one by one

Requests for each path over the 30 days. Some of these paths redirect to
another file on the reference site; the count is for the path as requested.

| Path | Requests | Crawlers |
|---|---:|---:|
| `/llms.txt` | 51 | 8 |
| `/news/changelog.json` | 36 | 4 |
| `/ai-discovery.json` | 30 | 4 |
| `/news/latest.json` | 27 | 2 |
| `/llms-full.txt` | 22 | 4 |
| `/news/archive.jsonl` | 21 | 3 |
| `/ai-discovery.md` | 18 | 5 |
| `/feed.json` | 18 | 3 |
| `/updates.json` | 16 | 2 |
| `/knowledge-graph.json` | 15 | 4 |
| `/news/llms.txt` | 14 | 2 |
| `/.well-known/ai.json` | 13 | 3 |
| `/news/speakable.json` | 13 | 2 |
| `/feed` | 11 | 4 |
| `/wiki/llms.txt` | 9 | 4 |
| `/opensearch.xml` | 7 | 1 |
| `/rss.xml` | 2 | 1 |
| `/blog-feed.xml` | 1 | 1 |
| `/mcp.json` | 1 | 1 |
| `/.well-known/agents.json` | 1 | 1 |
| `/api/v1/adp/stats` | 1 | 1 |

For comparison, the core files: `/robots.txt` 412, `/news-sitemap.xml` 342,
`/sitemap.xml` 264.

---

## Who reads the markdown copies

| Crawler | Operator | Requests for copies | Share of all copy requests |
|---|---|---:|---:|
| Meta-ExternalAgent | Meta | 4,355 | 82.3% |
| AhrefsBot | Ahrefs | 270 | 5.1% |
| SemrushBot | Semrush | 224 | 4.2% |
| Bytespider | ByteDance | 152 | 2.9% |
| PerplexityBot | Perplexity | 73 | 1.4% |
| YouBot | You.com | 73 | 1.4% |
| GPTBot | OpenAI | 70 | 1.3% |
| OAI-SearchBot | OpenAI | 39 | 0.7% |
| Amazonbot | Amazon | 18 | 0.3% |
| Others (DotBot, CCBot, ClaudeBot, ChatGPT-User) | | 16 | 0.3% |

One crawler accounts for four fifths of the copy traffic. Without it, the
copies would still draw about three times the requests of the root files
(935 against 327), from twelve crawlers.

---

## Every crawler in the window

| Crawler | Operator | All requests | HTML pages | Markdown copies | Root files | robots.txt and sitemaps |
|---|---|---:|---:|---:|---:|---:|
| Meta-ExternalAgent | Meta | 9,502 | 4,895 | 4,355 | 251 | 1 |
| PerplexityBot | Perplexity | 2,867 | 2,779 | 73 | 2 | 13 |
| Amazonbot | Amazon | 1,784 | 1,750 | 18 | 16 | 0 |
| SemrushBot | Semrush | 1,469 | 1,227 | 224 | 6 | 12 |
| ClaudeBot | Anthropic | 1,420 | 881 | 3 | 3 | 533 |
| AhrefsBot | Ahrefs | 1,010 | 664 | 270 | 13 | 63 |
| YouBot | You.com | 913 | 616 | 73 | 7 | 217 |
| Bytespider | ByteDance | 853 | 673 | 152 | 11 | 17 |
| CCBot | Common Crawl | 706 | 697 | 5 | 1 | 3 |
| ChatGPT-User | OpenAI | 541 | 538 | 2 | 1 | 0 |
| GPTBot | OpenAI | 447 | 305 | 70 | 8 | 64 |
| OAI-SearchBot | OpenAI | 426 | 288 | 39 | 5 | 94 |
| Sogou | Sogou | 138 | 136 | 0 | 2 | 0 |
| DotBot | Moz | 59 | 52 | 6 | 0 | 1 |
| cohere-ai | Cohere | 19 | 19 | 0 | 0 | 0 |
| Bingbot | Microsoft | 11 | 10 | 0 | 1 | 0 |
| Googlebot | Google | 2 | 1 | 0 | 0 | 1 |
| Claude-User | Anthropic | 1 | 1 | 0 | 0 | 0 |

**Fetchers that act for a person asking a question read pages.**
ChatGPT-User made 541 requests: 538 for HTML pages, 2 for markdown copies and
1 for a root file. The other requests in the table come from crawlers that
build an index or a training corpus.

---

## How the markdown copies came to be read

The copies went live on the reference site on 7 July 2026.

| Date | State of the site | Markdown copies as a share of crawler requests |
|---|---|---:|
| Up to 7 July 2026 | Root discovery files only | No copies yet. Root files: 0.75% of 142,458 requests since logging began |
| 11 July 2026 | Copies live for four days, announced in the page head only | 4.0% (241 of 6,018) |
| 11 July 2026 | Visible body link added to each page; copies added to the sitemap | |
| 9 August 2026 | 30 days later | 17.3% (5,383 of 31,176) |
| 24 September 2026 | Copies moved out of the main sitemap into a dedicated one that `robots.txt` does not name. Body links unchanged | |
| 12 November 2026 | This report | 23.9% (5,290 of 22,168) |

Crawlers found the copies within days once pages pointed at them, and the
share grew after the copies were linked from the page body and listed in the
sitemap. Those changes were made together, so July alone cannot separate them.

September can. On 24 September the copies were taken out of the main sitemap
(they are marked `noindex`, and listing them there drew search-console
warnings). They stayed linked from each page body.

- In the six full weeks before the move the copies drew between 17.5% and
  21.8% of crawler requests each week (15.8% in the week of the move). In
  the seven weeks after, between 22.0% and 30.2%.
- 18 copies that had never been requested before the move were requested
  after it, by ten crawlers including PerplexityBot, ClaudeBot, GPTBot and
  OAI-SearchBot.
- The dedicated sitemap was requested 31 times in the report window, by two
  crawlers (GPTBot and Meta-ExternalAgent).

The body link carries discovery. Level 1 therefore requires the body link and
only recommends a sitemap listing and the head link.

---

## What this does not show

- **It does not show that anything here earns a citation.** These are
  requests, not citations. A crawler reading a file is necessary for that file
  to matter and is not evidence that it does.
- **It is one site.** A site with different content, age or traffic may see a
  different mix.
- **Crawlers are identified by user agent.** A user agent is free text and can
  be forged. The reference site began checking crawler addresses against the
  operators' published ranges on 12 November 2026; this window predates that.
- **Most of the copy traffic is one crawler.** If Meta-ExternalAgent changes
  its behaviour, the headline share changes with it.
- **Requests are not reading.** A fetch says nothing about what was done with
  the content.

---

## Method

Every request whose user agent matches a known AI or search crawler is logged
with its path. For this report each request was put in one class:

- **Markdown copies:** paths under `/okf/`, where the reference site serves
  its copies.
- **robots.txt and sitemaps:** `/robots.txt`, `/sitemap.xml`,
  `/news-sitemap.xml`, `/sitemap-ai.xml`.
- **Root discovery files:** the paths in the table above.
- **HTML pages:** everything else.

To run the same measurement on your own site, log the user agent and path of
each request and group the paths the same way. The
[registry](registry/adp-registry.json) lists the paths to group.

---

## Withdrawn figures

Earlier versions of this page reported a 2.4 day average time to first
citation, a 100% citation rate, three anonymised case studies, per-query
success rates and referral revenue comparisons. They are withdrawn because
they cannot be substantiated. Nothing on this page replaces them with a
citation claim.
