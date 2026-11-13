# Quick Start: Level 1

Level 1 is the only required level. For each content page you publish a
markdown copy and link to it from the page. On a
site with a template system this is an afternoon's work.

Working files for every step are in [examples/level-1/](examples/level-1/).

---

## 1. Decide which pages are content pages

Content pages are the ones whose text you want an AI system to be able to
read and quote: articles, releases, product pages, documentation, reference
entries. Leave out search results, account pages, checkout and anything
behind a login.

## 2. Generate a markdown copy of each one

Render the copy from the same source as the page, so the two cannot disagree.

- Serve it at a stable URL: the page URL plus `.md`, or a parallel tree such
  as `/md/...`.
- Answer `200` with `Content-Type: text/markdown; charset=utf-8`.
- Include the title, the date, who published it and the full body text.
- Add front matter with the URL of the page it copies.
- Say nothing the page does not say.
- Send `X-Robots-Tag: noindex, follow` and
  `Link: <page URL>; rel="canonical"`, so search engines index the page and
  not its copy.

```markdown
---
title: Example Corporation opens a Dublin office
url: https://example.com/news/dublin-office
date: 2026-11-13
---

# Example Corporation opens a Dublin office

Example Corporation today opened an office in Dublin.
```

If your pages are already written in markdown, the copy is the source file
with front matter added.

## 3. Link to the copy from the page body

Add a visible link in the page template, and a head link beside it:

```html
<link rel="alternate" type="text/markdown" href="/news/dublin-office.md">
...
<p>For AI agents and developers:
  <a href="/news/dublin-office.md">this page as markdown</a>.</p>
```

The body link is the required one. Clients that work from extracted body text
never see the head.

## 4. Optionally, list the copies in a sitemap

Recommended, not required: crawlers find the copies through the body link.
If your copies are `noindex`, put them in a dedicated sitemap rather than the
main one.

```xml
<!-- /sitemap-md.xml -->
<url><loc>https://example.com/news/dublin-office.md</loc></url>
```

## 5. Check robots.txt

It needs a `Sitemap:` line and must not block the pages or the copies. Keep
the rules in one group with no blank lines inside it, and put `Disallow`
lines before a broad `Allow: /`: some parsers end a group at the first blank
line and take the first rule that matches.

```
User-agent: *
Disallow: /admin/
Allow: /

Sitemap: https://example.com/sitemap.xml
```

## 6. Audit it

```bash
pip install git+https://github.com/BuddySpuds/adp-audit-cli
adp-audit example.com
```

The tool samples pages from your sitemap and reports, for each, whether it
has a markdown copy that is linked from the body and crawlable.

## 7. Measure it

Log the user agent and path of each crawler request, and count requests for
your copies against requests for your pages. Section 9 of the
[specification](SPECIFICATION.md#9-measurement) lists what to record.
Expect days to weeks before crawlers pick the copies up.

---

## After Level 1

Levels 2 to 4 are optional and independent:

- **Level 2, site context:** `/llms.txt`, `/ai-discovery.json`,
  `/knowledge-graph.json`. Templates in [examples/level-2/](examples/level-2/).
- **Level 3, feeds and news:** `/feed.json`, `/rss.xml` and the news
  namespace in [docs/NEWS_NAMESPACE.md](docs/NEWS_NAMESPACE.md).
- **Level 4, agent actions:** an MCP manifest, in
  [section 10 of the specification](SPECIFICATION.md#10-mcp-integration-level-4---optional).

The measured request counts for each are in [RESULTS.md](RESULTS.md). Read
them before deciding how much to build.
