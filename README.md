# AI Discovery Protocol (ADP) v3.1

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.1-green.svg)](CHANGELOG.md)
[![Measured results](https://img.shields.io/badge/Results-measured-orange.svg)](RESULTS.md)

An open standard for publishing a website so that AI crawlers and agents can
read it. Version 3.1 is rebuilt around what crawler logs show they fetch.

---

## The short version

Give every content page a markdown copy, and link to the copy from the page
body. That is Level 1, and it is the only required level.

```html
<!-- on https://example.com/blog/our-launch -->
<link rel="alternate" type="text/markdown" href="/blog/our-launch.md">
...
<p>For AI agents and developers:
  <a href="/blog/our-launch.md">this page as markdown</a>.</p>
```

Everything else in the protocol (`llms.txt`, a meta-index, a knowledge graph,
feeds, agent manifests) is optional.

---

## Why it is built this way

Over 30 days the reference site logged 22,168 crawler requests.

| What was requested | Share of requests |
|---|---:|
| HTML pages | 70.1% |
| Markdown copies of pages | 23.9% |
| `robots.txt` and sitemaps | 4.6% |
| Root discovery files, all of them together | 1.5% |

Earlier versions of ADP made a root file, `/ai-discovery.json`, the required
entry point. Crawlers requested it 30 times in those 30 days. They requested
the per-page markdown copies 5,290 times. The protocol now follows the
behaviour. Full tables, method and limits: [RESULTS.md](RESULTS.md).

ADP does not promise citations. It describes how to publish content in a form
crawlers demonstrably fetch, and how to measure whether they do.

---

## Levels

<!-- registry:levels:start -->
| Level | Name | Status | What it is |
|---|---|---|---|
| 1 | Page copies | Required | Every content page has a markdown copy that is linked from the page body. |
| 2 | Site context | Optional | Root files that describe the site as a whole. |
| 3 | Feeds and news | Optional | Machine-readable streams of new and changed content. |
| 4 | Agent actions and measurement | Optional | Manifests that let an agent call tools on the site, and a public statistics endpoint. |
<!-- registry:levels:end -->

### Level 1: what each content page needs

<!-- registry:page:start -->
| Requirement | Status | Rule |
|---|---|---|
| `markdown_copy` | Required | The page has a markdown copy at a stable URL. The copy answers 200 with a text/markdown or text/plain content type and carries the same content as the page. |
| `body_link` | Required | The visible body of the page contains an ordinary link to its markdown copy. |
| `crawl_allowed` | Required | robots.txt does not block AI crawlers from the page or from its markdown copy. |
| `sitemap_listing` | Recommended | The markdown copy is listed in a sitemap: the main one, or a dedicated sitemap for copies when the copies are marked noindex. |
| `alternate_link` | Recommended | The page head carries `<link rel="alternate" type="text/markdown">` pointing at the copy. |
<!-- registry:page:end -->

A content page is any page whose text you want an AI system to be able to
read and quote: an article, a release, a product page, a reference entry.

### Endpoints

<!-- registry:endpoints:start -->
| Level | Path | Status | Purpose |
|---|---|---|---|
| 1 | `/robots.txt` | Required | Crawler directives, with a Sitemap line |
| 1 | `/sitemap.xml` | Required | Sitemap listing the content pages |
| 2 | `/llms.txt` | Optional | Plain-language overview of the site (llmstxt.org format) |
| 2 | `/llms-full.txt` | Optional | Long-form context document |
| 2 | `/llms-lite.txt` | Optional | Condensed context document |
| 2 | `/ai-discovery.json` | Optional | Meta-index of the site's machine-readable resources |
| 2 | `/ai-discovery.md` | Optional | Markdown rendering of the meta-index |
| 2 | `/knowledge-graph.json` | Optional | Schema.org entity catalogue as JSON-LD |
| 2 | `/.well-known/ai.json` | Optional | Well-known pointer to the meta-index |
| 2 | `/opensearch.xml` | Optional | OpenSearch description of the site search |
| 3 | `/feed.json` | Optional | JSON Feed of recent content |
| 3 | `/rss.xml` | Optional | RSS feed of recent content |
| 3 | `/updates.json` | Optional | Recent changes |
| 3 | `/api/v1/webhooks/discovery` | Optional | Webhook registration for content updates |
| 3 | `/news/llms.txt` | Optional | Context document for the news section |
| 3 | `/news/speakable.json` | Optional | Short spoken-form summaries |
| 3 | `/news/changelog.json` | Optional | Dated list of additions and corrections |
| 3 | `/news/archive.jsonl` | Optional | Full archive, one JSON object per line |
| 4 | `/mcp.json` | Optional | Model Context Protocol server manifest |
| 4 | `/.well-known/agents.json` | Optional | Agent capability declaration |
| 4 | `/api/v1/adp/stats` | Optional | Public crawler-visit statistics |
<!-- registry:endpoints:end -->

This table is generated from
[registry/adp-registry.json](registry/adp-registry.json), the one
machine-readable list of levels, requirements and endpoints. The audit tool
and the reference implementation read the same file.

---

## Check a site

[adp-audit-cli](https://github.com/BuddySpuds/adp-audit-cli) reads the
registry and reports which level a site meets:

```bash
adp-audit example.com
```

It samples pages from the sitemap, checks each for a linked, crawlable
markdown copy, then reports which optional endpoints are served.

```bash
pip install git+https://github.com/BuddySpuds/adp-audit-cli
```

---

## Measure it

Log the user agent and path of every crawler request and group the paths by
level. Section 9 of the [specification](SPECIFICATION.md) describes the
logging, and [RESULTS.md](RESULTS.md) shows the output for the reference
site. If you publish your own numbers, open an issue: a second and third site
would make the evidence much stronger than one.

---

## Reference implementation

[pressonify.ai](https://pressonify.ai) serves a markdown copy of every press
release, article, topic and organisation page under `/okf/` and links each
copy from the page body. The copies are marked `noindex` with a canonical
link to their page, and are listed in a dedicated sitemap. It also serves
the optional Level 2 to 4 endpoints.

---

## Documentation

| Document | What it covers |
|---|---|
| [SPECIFICATION.md](SPECIFICATION.md) | The full specification |
| [QUICK_START.md](QUICK_START.md) | Level 1 in an afternoon |
| [RESULTS.md](RESULTS.md) | Measured crawler behaviour, method and limits |
| [FAQ.md](FAQ.md) | Common questions |
| [registry/adp-registry.json](registry/adp-registry.json) | Machine-readable levels and endpoints |
| [examples/](examples/) | A Level 1 page and optional Level 2 files |
| [docs/NEWS_NAMESPACE.md](docs/NEWS_NAMESPACE.md) | Optional news endpoints |
| [docs/PROOF_INFRASTRUCTURE.md](docs/PROOF_INFRASTRUCTURE.md) | Crawler logging and citation checks |
| [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md) | Reasoning behind versions 1.0 to 3.0 |
| [CHANGELOG.md](CHANGELOG.md) | Version history |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The most useful contribution is data:
crawler logs from another site, grouped as in [RESULTS.md](RESULTS.md).

## License

MIT. See [LICENSE](LICENSE) and [INTELLECTUAL_PROPERTY.md](INTELLECTUAL_PROPERTY.md).
