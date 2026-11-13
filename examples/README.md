# Examples

Example Corporation is fictional. Every fact in these files is placeholder
text: replace all of it with your own.

## level-1/ (required)

One content page with its markdown copy, the sitemap that lists both, and a
`robots.txt` that names the sitemap.

| File | Serve it at | What to notice |
|---|---|---|
| `page.html` | `/news/dublin-office` | The visible body link to the copy, and the head `rel="alternate"` link |
| `page.md` | `/news/dublin-office.md` | Same content as the page, front matter with the page URL. Serve as `text/markdown` |
| `sitemap.xml` | `/sitemap.xml` | The page and its copy each have an entry |
| `robots.txt` | `/robots.txt` | One group, a `Sitemap:` line, nothing blocking the page or the copy |

Check the result with [adp-audit-cli](https://github.com/BuddySpuds/adp-audit-cli):

```bash
adp-audit example.com
```

## level-2/ (optional)

Root files that describe the site as a whole: `ai-discovery.json`,
`knowledge-graph.json` and `llms.txt`. On the reference site all Level 2
files together drew under 1% of crawler requests in the measured month
([RESULTS.md](../RESULTS.md)), so build Level 1 first.

Formats for the Level 3 and Level 4 endpoints are in
[SPECIFICATION.md](../SPECIFICATION.md) and
[docs/NEWS_NAMESPACE.md](../docs/NEWS_NAMESPACE.md).
