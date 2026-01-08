# News Namespace Documentation

**ADP v2.1 Feature**

The `/news/` namespace provides specialized endpoints for news publishers, press release platforms, and content sites that need to optimize their news content for AI discovery.

---

## Overview

Traditional news content presents challenges for AI systems:
- Time-sensitive content that needs frequent updates
- Voice assistant optimization for audio reading
- Historical archives that grow continuously
- Version tracking for platform updates

The news namespace solves these with four specialized endpoints.

---

## Endpoints

### `/news/llms.txt`

News-specific context document focusing on recent content, headlines, and breaking news.

**Format:** Markdown
**Update Frequency:** Hourly to Daily
**Size:** 2-10KB

**Example:**

```markdown
# Pressonify News

> The latest press releases and announcements

## Breaking News

1. **TechCorp Raises $50M Series B** (Jan 8, 2026)
   TechCorp announced a $50 million Series B round led by Acme Ventures...
   URL: /news/techcorp-series-b-50m

2. **GreenEnergy Launches Solar Initiative** (Jan 7, 2026)
   GreenEnergy unveiled a new solar panel program for residential customers...
   URL: /news/greenenergy-solar-initiative

3. **HealthPlus FDA Approval** (Jan 6, 2026)
   HealthPlus received FDA approval for their new diagnostic device...
   URL: /news/healthplus-fda-approval

## Categories

- Technology (45 articles)
- Healthcare (32 articles)
- Finance (28 articles)
- Sustainability (19 articles)

## Archive

Full archive available at /news/archive.jsonl (streaming format)

---
*AI Discovery Protocol v2.1 | News Namespace*
*Updated: 2026-01-08T12:00:00Z*
```

**HTTP Headers:**
```
Content-Type: text/markdown; charset=utf-8
ETag: W/"news-abc123"
X-Update-Frequency: hourly
Cache-Control: public, max-age=900
```

---

### `/news/speakable.json`

Voice assistant-optimized content using Schema.org's Speakable specification. This endpoint provides text specifically formatted for text-to-speech systems like Google Assistant, Alexa, and Siri.

**Format:** JSON (Schema.org Speakable)
**Update Frequency:** Hourly
**Use Case:** Voice search, smart speakers, accessibility

**Example:**

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Speakable News Headlines",
  "description": "Voice-optimized news summaries",
  "numberOfItems": 10,
  "itemListElement": [
    {
      "@type": "NewsArticle",
      "position": 1,
      "headline": "TechCorp Raises 50 Million Dollar Series B",
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": [".headline", ".summary"]
      },
      "speakableText": "TechCorp has raised 50 million dollars in Series B funding. The round was led by Acme Ventures with participation from existing investors. The funds will be used to expand into European markets.",
      "url": "https://pressonify.ai/news/techcorp-series-b-50m",
      "datePublished": "2026-01-08T10:00:00Z",
      "publisher": {
        "@type": "Organization",
        "name": "Pressonify"
      }
    },
    {
      "@type": "NewsArticle",
      "position": 2,
      "headline": "GreenEnergy Launches Residential Solar Program",
      "speakableText": "GreenEnergy has launched a new solar panel program for homeowners. The program offers zero down payment installations with 25 year warranties. Interested customers can sign up on their website.",
      "url": "https://pressonify.ai/news/greenenergy-solar-initiative",
      "datePublished": "2026-01-07T14:00:00Z"
    }
  ]
}
```

**Key Fields:**
- `speakableText`: Plain text optimized for TTS (no abbreviations, spelled-out numbers)
- `headline`: Short, clear headline for voice reading
- `position`: Order for sequential reading

**Best Practices:**
1. Keep `speakableText` under 200 words
2. Spell out numbers ("50 million" not "$50M")
3. Avoid abbreviations and acronyms
4. Use simple sentence structures
5. Include the most important information first

---

### `/news/changelog.json`

Platform version history and updates. Useful for AI systems tracking when features changed or were added.

**Format:** JSON
**Update Frequency:** On release
**Use Case:** Version tracking, feature discovery, debugging

**Example:**

```json
{
  "version": "2.1",
  "platform": "Pressonify",
  "currentVersion": "2.9.6",
  "lastUpdated": "2026-01-07T20:00:00Z",
  "changelog": [
    {
      "version": "2.9.6",
      "date": "2026-01-07",
      "title": "Wide-Net Citation Detection",
      "type": "feature",
      "changes": [
        "Implemented wide-net query strategy for citation detection",
        "Added daily citation report at 8pm GMT",
        "Query success rate improved from 13% to 48%"
      ]
    },
    {
      "version": "2.9.5",
      "date": "2026-01-03",
      "title": "News AI Discoverability Sprint",
      "type": "feature",
      "changes": [
        "Added /news/llms.txt endpoint",
        "Added /news/speakable.json for voice assistants",
        "Added /news/changelog.json (this endpoint)",
        "Added /news/archive.jsonl for historical streaming",
        "Added /opensearch.xml for browser integration",
        "Expanded from 11 to 17 ADP endpoints"
      ]
    },
    {
      "version": "2.9.4",
      "date": "2026-01-01",
      "title": "AI Citability Enhancements",
      "type": "feature",
      "changes": [
        "Query Research Agent for variant generation",
        "Snippet-ready zones for AI extraction",
        "E-E-A-T structured fields",
        "PR-to-citation attribution"
      ]
    }
  ],
  "releaseTypes": {
    "feature": "New functionality added",
    "fix": "Bug fixes",
    "breaking": "Breaking changes",
    "security": "Security updates"
  }
}
```

---

### `/news/archive.jsonl`

Historical content archive in JSONL (JSON Lines) streaming format. Each line is a complete JSON object, allowing efficient streaming and processing of large archives.

**Format:** JSONL (newline-delimited JSON)
**Update Frequency:** On publish
**Use Case:** Historical analysis, bulk processing, AI training data

**Example:**

```
{"id":"pr_001","type":"press_release","headline":"TechCorp Raises $50M Series B","company":"TechCorp","url":"/news/techcorp-series-b-50m","publishedAt":"2026-01-08T10:00:00Z","category":"technology","wordCount":450}
{"id":"pr_002","type":"press_release","headline":"GreenEnergy Solar Initiative","company":"GreenEnergy","url":"/news/greenenergy-solar-initiative","publishedAt":"2026-01-07T14:00:00Z","category":"sustainability","wordCount":380}
{"id":"pr_003","type":"press_release","headline":"HealthPlus FDA Approval","company":"HealthPlus","url":"/news/healthplus-fda-approval","publishedAt":"2026-01-06T09:00:00Z","category":"healthcare","wordCount":520}
```

**Record Schema:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier |
| `type` | string | Content type (press_release, blog, etc.) |
| `headline` | string | Article headline |
| `company` | string | Company name (if applicable) |
| `url` | string | Relative URL path |
| `publishedAt` | ISO 8601 | Publication timestamp |
| `category` | string | Content category |
| `wordCount` | integer | Article word count |

**HTTP Headers:**
```
Content-Type: application/x-ndjson
Transfer-Encoding: chunked
X-Total-Records: 1250
```

**Processing Example (Python):**

```python
import httpx
import json

async def process_archive():
    async with httpx.AsyncClient() as client:
        async with client.stream('GET', 'https://example.com/news/archive.jsonl') as response:
            async for line in response.aiter_lines():
                if line:
                    record = json.loads(line)
                    # Process each record
                    print(f"Processing: {record['headline']}")
```

---

## Implementation Guide

### FastAPI Example

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse
from datetime import datetime
import json

app = FastAPI()

@app.get("/news/llms.txt")
async def news_llms_txt():
    content = generate_news_context()
    return Response(
        content=content,
        media_type="text/markdown",
        headers={
            "ETag": f'W/"{hash(content)}"',
            "X-Update-Frequency": "hourly"
        }
    )

@app.get("/news/speakable.json")
async def news_speakable():
    articles = get_recent_articles(limit=10)
    speakable_items = [
        {
            "@type": "NewsArticle",
            "position": i + 1,
            "headline": art.headline,
            "speakableText": generate_speakable_text(art),
            "url": art.url,
            "datePublished": art.published_at.isoformat()
        }
        for i, art in enumerate(articles)
    ]

    return JSONResponse({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "numberOfItems": len(speakable_items),
        "itemListElement": speakable_items
    })

@app.get("/news/archive.jsonl")
async def news_archive():
    async def generate():
        articles = get_all_articles()
        for article in articles:
            yield json.dumps({
                "id": article.id,
                "headline": article.headline,
                "url": article.url,
                "publishedAt": article.published_at.isoformat()
            }) + "\n"

    return StreamingResponse(
        generate(),
        media_type="application/x-ndjson"
    )
```

---

## Best Practices

### Content Freshness
- Update `/news/llms.txt` at least hourly during active news periods
- Update `/news/speakable.json` whenever new content is published
- Archive grows continuously; no need to update existing records

### Voice Optimization
- Test speakable content with actual TTS systems
- Avoid complex sentences that sound awkward when spoken
- Include pronunciation hints for unusual names or terms

### Archive Management
- Include metadata that helps AI systems filter relevant content
- Consider pagination for very large archives (100K+ records)
- Maintain consistent schema across all records

### HTTP Headers
- Always include `ETag` for cache validation
- Use `X-Update-Frequency` to hint at crawl scheduling
- Enable CORS for cross-origin AI tool access

---

## Reference Implementation

Live examples at Pressonify.ai:
- https://pressonify.ai/news/llms.txt
- https://pressonify.ai/news/speakable.json
- https://pressonify.ai/news/changelog.json
- https://pressonify.ai/news/archive.jsonl

---

*AI Discovery Protocol v2.1 - News Namespace*
*Maintained by [Pressonify](https://pressonify.ai)*
