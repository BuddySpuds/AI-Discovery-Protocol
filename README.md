# AI Discovery Protocol (ADP) v3.1

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.1-green.svg)](CHANGELOG.md)
[![Measured results](https://img.shields.io/badge/Results-measured-orange.svg)](RESULTS.md)

An open standard for publishing a website so that AI crawlers and agents can
read it. Version 3.1 is rebuilt around what crawler logs show they fetch.

---

## The short version

Give every content page a markdown copy. Link to the copy from the page body.
List the copy in your sitemap. That is Level 1, and it is the only required
level.

```html
<!-- on https://example.com/blog/our-launch -->
<link rel="alternate" type="text/markdown" href="/blog/our-launch.md">
...
<p>For AI agents and developers:
  <a href="/blog/our-launch.md">this page as markdown</a>.</p>
```

```xml
<!-- in sitemap.xml -->
<url><loc>https://example.com/blog/our-launch</loc></url>
<url><loc>https://example.com/blog/our-launch.md</loc></url>
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
<!-- registry:levels:end -->

### Level 1: what each content page needs

<!-- registry:page:start -->
<!-- registry:page:end -->

A content page is any page whose text you want an AI system to be able to
read and quote: an article, a release, a product page, a reference entry.

### Endpoints

<!-- registry:endpoints:start -->
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

It samples pages from the sitemap, checks each for a linked and listed
markdown copy, then reports which optional endpoints are served.

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
release, article, topic and organisation page under `/okf/`, links each copy
from the page body, and lists the copies in `/sitemap.xml`. It also serves the
optional Level 2 to 4 endpoints.

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
