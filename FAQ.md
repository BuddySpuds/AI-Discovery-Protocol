# Frequently Asked Questions

## What is ADP?

An open specification for publishing a website so that AI crawlers and agents
can read it. Its one required level is a markdown copy of every content page,
linked from the page body.

## Will implementing ADP get my site cited by ChatGPT, Claude or Perplexity?

Nobody can promise that, and ADP does not. What the evidence shows is which
files crawlers request. Whether an AI system then cites a page depends on the
question asked, the content, and what else has been published on the subject.

## What evidence is the protocol based on?

Request logs from the reference implementation, published in
[RESULTS.md](RESULTS.md) with the method and its limits. It is one site.
Logs from other sites are the most useful contribution anyone can make.

## Why did the required level change in v3.1?

Versions 1.0 to 3.0 required `/ai-discovery.json` as a single entry point. In
a month of logs it was requested 30 times, while per-page markdown copies
were requested 5,290 times. A required file that crawlers do not fetch was
the wrong thing to require.

## Should I still publish llms.txt, ai-discovery.json and a knowledge graph?

They are optional. They cost little to serve once generated, and crawler
behaviour changes, so there is a case for keeping them current. There is no
measured case for building them before Level 1.

## Why a body link? Is the head link not enough?

Some clients work from the extracted body text of a page and never see
`<head>` elements or HTTP headers. On the reference site, copies that were
linked from the page body but absent from the main sitemap were still found
by ten crawlers; see the timeline in [RESULTS.md](RESULTS.md).

## Does the markdown copy create duplicate content?

The copy is a different format of the same document. Put the page URL in the
copy's front matter so that a reader of the copy cites the page. To keep
search engines indexing only the page, serve the copy with
`X-Robots-Tag: noindex, follow` and a canonical `Link` header. The reference
site does both, and AI crawlers still fetch its copies.

## What about content negotiation (Accept: text/markdown)?

Serving markdown from the page URL when a client asks for it is a reasonable
idea that the protocol does not yet require, because we have not measured how
many clients ask. Section 9 of the specification asks implementers to log the
`Accept` header so that the question can be answered with data.

## Which pages count as content pages?

You decide. As a guide: pages whose text you would be glad to see quoted.

## How do I check my site?

Run [adp-audit-cli](https://github.com/BuddySpuds/adp-audit-cli). It reads
the same [registry](registry/adp-registry.json) as this specification.

## How do I know crawlers are reading the copies?

Log crawler requests by path ([specification, section 9](SPECIFICATION.md#9-measurement)).
A user agent can be forged, so where an operator publishes its address
ranges, check against them.

## Can I block AI crawlers and still conform?

Level 1 requires that `robots.txt` does not block AI crawlers from content
pages or their copies. A site that blocks them has made a legitimate choice,
and ADP is not for that site.

## Is there a cost or a licence?

No cost. The specification is MIT licensed. See
[INTELLECTUAL_PROPERTY.md](INTELLECTUAL_PROPERTY.md).

## Who maintains it?

[Pressonify.ai](https://pressonify.ai), which also runs the reference
implementation. Issues and pull requests are welcome; see
[CONTRIBUTING.md](CONTRIBUTING.md).
