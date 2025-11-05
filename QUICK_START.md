# AI Discovery Protocol - Quick Start Guide

**Get your website AI-discoverable in 15 minutes**

---

## Why Should I Care?

When users ask ChatGPT, Claude, or Perplexity about topics related to your business, **your website should appear in the results**. Right now, it probably doesn't.

The AI Discovery Protocol (ADP) makes your content discoverable to AI systems.

---

## Implementation Levels

### Level 1: Minimal (15 minutes)
- **Just** `ai-discovery.json`
- Signals AI-friendly intent
- Good: Basic discoverability

### Level 2: Standard (2-4 hours) **← RECOMMENDED**
- `ai-discovery.json` + `knowledge-graph.json` + `llms.txt`
- Full AI discoverability
- Great: Competitive advantage

### Level 3: Advanced (1-2 days)
- All Level 2 files + versioning + change logs
- Incremental crawling support
- Best: Future-proof

---

## Level 1: Minimal Implementation (15 Minutes)

### Step 1: Create ai-discovery.json

Create a file named `ai-discovery.json` in your site's root directory:

```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "website": {
    "url": "https://yoursite.com",
    "name": "Your Company Name",
    "description": "Brief description of what you do"
  }
}
```

**Replace:**
- `https://yoursite.com` → Your actual website URL
- `Your Company Name` → Your company/brand name
- `Brief description...` → One sentence about your business
- `2025-11-02T12:00:00Z` → Current timestamp (ISO 8601 format)

---

### Step 2: Upload to Your Server

#### Static Site (Netlify, Vercel, GitHub Pages)
```bash
# Copy to your public directory
cp ai-discovery.json public/

# Deploy
git add public/ai-discovery.json
git commit -m "Add AI Discovery Protocol support"
git push
```

#### WordPress
1. Use FTP or cPanel File Manager
2. Upload `ai-discovery.json` to root directory (same level as `wp-config.php`)
3. Verify: `https://yoursite.com/ai-discovery.json`

#### Custom Server (Node.js, FastAPI, etc.)
Create an endpoint that serves the JSON:

**FastAPI Example:**
```python
@app.get("/ai-discovery.json")
async def ai_discovery():
    return {
        "version": "1.0.0",
        "generatedAt": datetime.utcnow().isoformat() + "Z",
        "website": {
            "url": "https://yoursite.com",
            "name": "Your Company",
            "description": "Description here"
        }
    }
```

**Express.js Example:**
```javascript
app.get('/ai-discovery.json', (req, res) => {
  res.json({
    version: '1.0.0',
    generatedAt: new Date().toISOString(),
    website: {
      url: 'https://yoursite.com',
      name: 'Your Company',
      description: 'Description here'
    }
  });
});
```

---

### Step 3: Verify

```bash
curl https://yoursite.com/ai-discovery.json | jq
```

**Expected output:**
```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "website": {
    "url": "https://yoursite.com",
    "name": "Your Company Name",
    "description": "Brief description"
  }
}
```

**✅ Done!** You've implemented Level 1 ADP.

---

## Level 2: Standard Implementation (2-4 Hours)

This is the **recommended implementation** for most websites.

### Step 1: Create knowledge-graph.json

**Template for E-commerce Store:**

```json
{
  "@context": "https://schema.org",
  "@type": "KnowledgeGraph",
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "statistics": {
    "totalEntities": 3,
    "byType": {
      "Organization": 1,
      "Product": 2
    }
  },
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://yourstore.com/#organization",
      "name": "Your Store Name",
      "url": "https://yourstore.com",
      "logo": "https://yourstore.com/logo.png",
      "description": "Brief company description",
      "sameAs": [
        "https://twitter.com/yourstore",
        "https://facebook.com/yourstore",
        "https://instagram.com/yourstore"
      ]
    },
    {
      "@type": "Product",
      "@id": "https://yourstore.com/products/product-1",
      "name": "Product 1 Name",
      "description": "Product description",
      "image": "https://yourstore.com/images/product-1.jpg",
      "brand": {
        "@id": "https://yourstore.com/#organization"
      },
      "offers": {
        "@type": "Offer",
        "price": "29.99",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "url": "https://yourstore.com/products/product-1"
      }
    },
    {
      "@type": "Product",
      "@id": "https://yourstore.com/products/product-2",
      "name": "Product 2 Name",
      "description": "Product description",
      "image": "https://yourstore.com/images/product-2.jpg",
      "brand": {
        "@id": "https://yourstore.com/#organization"
      },
      "offers": {
        "@type": "Offer",
        "price": "49.99",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "url": "https://yourstore.com/products/product-2"
      }
    }
  ]
}
```

**Template for SaaS Company:**

```json
{
  "@context": "https://schema.org",
  "@type": "KnowledgeGraph",
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "statistics": {
    "totalEntities": 2,
    "byType": {
      "Organization": 1,
      "SoftwareApplication": 1
    }
  },
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://yourapp.com/#organization",
      "name": "Your SaaS Company",
      "url": "https://yourapp.com",
      "logo": "https://yourapp.com/logo.png",
      "description": "Brief company description"
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://yourapp.com/#software",
      "name": "Your App Name",
      "applicationCategory": "BusinessApplication",
      "description": "What your app does",
      "offers": {
        "@type": "Offer",
        "price": "49",
        "priceCurrency": "USD"
      },
      "operatingSystem": "Web Browser",
      "url": "https://yourapp.com"
    }
  ]
}
```

**Template for Blog/Publisher:**

```json
{
  "@context": "https://schema.org",
  "@type": "KnowledgeGraph",
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "statistics": {
    "totalEntities": 4,
    "byType": {
      "Organization": 1,
      "NewsArticle": 3
    }
  },
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://yourblog.com/#organization",
      "name": "Your Blog Name",
      "url": "https://yourblog.com",
      "logo": "https://yourblog.com/logo.png"
    },
    {
      "@type": "NewsArticle",
      "@id": "https://yourblog.com/posts/article-1",
      "headline": "Article 1 Title",
      "description": "Article description",
      "datePublished": "2025-11-01T09:00:00Z",
      "author": {
        "@type": "Person",
        "name": "Author Name"
      },
      "publisher": {
        "@id": "https://yourblog.com/#organization"
      },
      "url": "https://yourblog.com/posts/article-1"
    },
    {
      "@type": "NewsArticle",
      "@id": "https://yourblog.com/posts/article-2",
      "headline": "Article 2 Title",
      "description": "Article description",
      "datePublished": "2025-10-28T14:00:00Z",
      "author": {
        "@type": "Person",
        "name": "Author Name"
      },
      "publisher": {
        "@id": "https://yourblog.com/#organization"
      },
      "url": "https://yourblog.com/posts/article-2"
    },
    {
      "@type": "NewsArticle",
      "@id": "https://yourblog.com/posts/article-3",
      "headline": "Article 3 Title",
      "description": "Article description",
      "datePublished": "2025-10-25T10:00:00Z",
      "author": {
        "@type": "Person",
        "name": "Author Name"
      },
      "publisher": {
        "@id": "https://yourblog.com/#organization"
      },
      "url": "https://yourblog.com/posts/article-3"
    }
  ]
}
```

**Upload** this file to your site's root directory.

---

### Step 2: Create llms.txt

Create a file named `llms.txt` with this structure:

```markdown
---
version: 1.0.0
lastModified: 2025-11-02T12:00:00Z
---

# Your Company/Site Name

> AI-Optimized Content for Large Language Models

## Overview

[2-3 sentences about your business/site. What do you do? Who do you serve?]

Founded in [year], we [mission statement]. We serve [target customers] with [products/services].

## Products/Services

### [Product/Service 1 Name]
- **Description:** [What it is]
- **Price:** $X USD
- **Use Cases:** [Who it's for]
- **Link:** https://yoursite.com/product-1

### [Product/Service 2 Name]
- **Description:** [What it is]
- **Price:** $Y USD
- **Use Cases:** [Who it's for]
- **Link:** https://yoursite.com/product-2

## Recent Updates

### [Latest News/Update 1] (November 1, 2025)
[Brief summary of announcement, product launch, etc.]

Read more: https://yoursite.com/news/update-1

### [Update 2] (October 28, 2025)
[Brief summary]

Read more: https://yoursite.com/news/update-2

## Key Features

- [Feature 1]: [Brief description]
- [Feature 2]: [Brief description]
- [Feature 3]: [Brief description]

## Contact & Links

- **Website:** https://yoursite.com
- **Email:** contact@yoursite.com
- **Documentation:** https://docs.yoursite.com (if applicable)
- **Support:** https://yoursite.com/support

---
*Last updated: November 2, 2025*
```

**Tips:**
- Keep it under 10KB (context window limits)
- Update monthly or when major changes occur
- Include recent blog posts/press releases
- Link to full content for details

**Upload** this file to your site's root directory.

---

### Step 3: Update ai-discovery.json

Update your `ai-discovery.json` to reference the new files:

```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "website": {
    "url": "https://yoursite.com",
    "name": "Your Company Name",
    "description": "Brief description"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://yoursite.com/knowledge-graph.json",
      "format": "application/ld+json",
      "entityCount": 10,
      "version": "1.0.0"
    },
    "contextDocument": {
      "url": "https://yoursite.com/llms.txt",
      "format": "text/markdown"
    }
  }
}
```

**Replace:**
- `entityCount`: Number of entities in your knowledge graph
- URLs: Your actual domain

---

### Step 4: Update robots.txt (Optional)

Add these lines to your `robots.txt`:

```
# AI Discovery Protocol
# Learn more: https://github.com/pressonify/ai-discovery-protocol

# AI-Optimized Endpoints
Allow: /ai-discovery.json
Allow: /knowledge-graph.json
Allow: /llms.txt

# Standard rules
User-agent: *
Allow: /

# AI Crawlers
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /
```

---

### Step 5: Verify

```bash
# Check ai-discovery.json
curl https://yoursite.com/ai-discovery.json | jq

# Check knowledge-graph.json
curl https://yoursite.com/knowledge-graph.json | jq

# Check llms.txt
curl https://yoursite.com/llms.txt
```

**✅ Done!** You've implemented Level 2 ADP.

---

## Level 3: Advanced Implementation (1-2 Days)

### Add Versioning to Knowledge Graph

Update your `knowledge-graph.json` with versioning:

```json
{
  "@context": "https://schema.org",
  "@type": "KnowledgeGraph",
  "version": "1.0.1",
  "generatedAt": "2025-11-02T12:00:00Z",
  "changeLog": {
    "lastModified": "2025-11-02T12:00:00Z",
    "changes": [
      {
        "timestamp": "2025-11-02T12:00:00Z",
        "entityType": "Product",
        "entityId": "https://yoursite.com/products/widget-pro",
        "changeType": "updated",
        "modifiedFields": ["price", "availability"]
      },
      {
        "timestamp": "2025-11-01T09:00:00Z",
        "entityType": "NewsArticle",
        "entityId": "https://yoursite.com/news/product-launch",
        "changeType": "created"
      }
    ]
  },
  "statistics": {
    "totalEntities": 10,
    "byType": {
      "Organization": 1,
      "Product": 5,
      "NewsArticle": 4
    }
  },
  "@graph": [ /* entities */ ]
}
```

### Add Capability Flags

Update your `ai-discovery.json`:

```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-02T12:00:00Z",
  "website": { /* ... */ },
  "endpoints": { /* ... */ },
  "capabilities": {
    "supportsVersioning": true,
    "supportsIncrementalUpdates": true,
    "supportsChangeDetection": true,
    "updateFrequency": "daily"
  }
}
```

**✅ Done!** You've implemented Level 3 ADP.

---

## Automation Scripts

### Shopify (Liquid Template)

Generate `knowledge-graph.json` dynamically:

```liquid
{
  "@context": "https://schema.org",
  "@type": "KnowledgeGraph",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "{{ shop.url }}/#organization",
      "name": "{{ shop.name }}",
      "url": "{{ shop.url }}"
    }
    {% for product in collections.all.products limit: 50 %}
    ,{
      "@type": "Product",
      "@id": "{{ shop.url }}{{ product.url }}",
      "name": "{{ product.title }}",
      "description": "{{ product.description | strip_html }}",
      "image": "{{ product.featured_image.src }}",
      "offers": {
        "@type": "Offer",
        "price": "{{ product.price | money_without_currency }}",
        "priceCurrency": "{{ shop.currency }}",
        "availability": "{% if product.available %}https://schema.org/InStock{% else %}https://schema.org/OutOfStock{% endif %}",
        "url": "{{ shop.url }}{{ product.url }}"
      }
    }
    {% endfor %}
  ]
}
```

---

### WordPress (PHP)

```php
<?php
// Add to functions.php

add_action('init', 'adp_rewrite_rules');
function adp_rewrite_rules() {
    add_rewrite_rule('^ai-discovery\.json$', 'index.php?adp=discovery', 'top');
    add_rewrite_rule('^knowledge-graph\.json$', 'index.php?adp=knowledge', 'top');
}

add_filter('query_vars', 'adp_query_vars');
function adp_query_vars($vars) {
    $vars[] = 'adp';
    return $vars;
}

add_action('template_redirect', 'adp_template_redirect');
function adp_template_redirect() {
    $adp = get_query_var('adp');

    if ($adp === 'discovery') {
        header('Content-Type: application/json');
        echo json_encode([
            'version' => '1.0.0',
            'generatedAt' => current_time('c'),
            'website' => [
                'url' => get_site_url(),
                'name' => get_bloginfo('name'),
                'description' => get_bloginfo('description')
            ]
        ]);
        exit;
    }

    if ($adp === 'knowledge') {
        header('Content-Type: application/ld+json');

        $posts = get_posts(['numberposts' => 50]);
        $graph = [
            [
                '@type' => 'Organization',
                '@id' => get_site_url() . '/#organization',
                'name' => get_bloginfo('name'),
                'url' => get_site_url()
            ]
        ];

        foreach ($posts as $post) {
            $graph[] = [
                '@type' => 'NewsArticle',
                '@id' => get_permalink($post->ID),
                'headline' => $post->post_title,
                'datePublished' => get_the_date('c', $post->ID),
                'url' => get_permalink($post->ID)
            ];
        }

        echo json_encode([
            '@context' => 'https://schema.org',
            '@type' => 'KnowledgeGraph',
            '@graph' => $graph
        ]);
        exit;
    }
}

// Flush rewrite rules on plugin activation
flush_rewrite_rules();
?>
```

---

### FastAPI (Python)

```python
from fastapi import FastAPI
from datetime import datetime
from typing import List

app = FastAPI()

@app.get("/ai-discovery.json")
async def ai_discovery():
    return {
        "version": "1.0.0",
        "generatedAt": datetime.utcnow().isoformat() + "Z",
        "website": {
            "url": "https://yoursite.com",
            "name": "Your Company",
            "description": "Description"
        },
        "endpoints": {
            "knowledgeGraph": {
                "url": "https://yoursite.com/knowledge-graph.json",
                "format": "application/ld+json",
                "entityCount": await get_entity_count(),
                "version": "1.0.0"
            }
        }
    }

@app.get("/knowledge-graph.json")
async def knowledge_graph():
    entities = await fetch_entities_from_database()

    return {
        "@context": "https://schema.org",
        "@type": "KnowledgeGraph",
        "version": "1.0.0",
        "generatedAt": datetime.utcnow().isoformat() + "Z",
        "statistics": {
            "totalEntities": len(entities),
            "byType": count_by_type(entities)
        },
        "@graph": entities
    }

async def fetch_entities_from_database():
    # Your database logic here
    return [
        {
            "@type": "Organization",
            "@id": "https://yoursite.com/#organization",
            "name": "Your Company"
        }
    ]
```

---

## Testing & Validation

### Manual Testing

```bash
# Test ai-discovery.json
curl -H "Accept: application/json" https://yoursite.com/ai-discovery.json | jq

# Test knowledge-graph.json
curl -H "Accept: application/ld+json" https://yoursite.com/knowledge-graph.json | jq

# Test llms.txt
curl https://yoursite.com/llms.txt

# Check HTTP headers
curl -I https://yoursite.com/ai-discovery.json
```

**Expected headers:**
```
HTTP/2 200
content-type: application/json
cache-control: public, max-age=3600
last-modified: Sat, 02 Nov 2025 12:00:00 GMT
```

---

### JSON Schema Validation

Coming soon: Online validator at https://pressonify.ai/tools/adp-validator

For now, use `jsonschema` CLI:

```bash
npm install -g jsonschema

jsonschema -i ai-discovery.json \
  https://pressonify.ai/schemas/ai-discovery/v1.0.json
```

---

## Common Mistakes

### ❌ Wrong: Including sensitive data
```json
{
  "database": "postgresql://user:password@localhost/db",
  "apiKey": "sk-..."
}
```

### ✅ Right: Only public information
```json
{
  "website": {
    "url": "https://yoursite.com",
    "name": "Your Company"
  }
}
```

---

### ❌ Wrong: Relative URLs
```json
{
  "knowledgeGraph": {
    "url": "/knowledge-graph.json"
  }
}
```

### ✅ Right: Absolute URLs
```json
{
  "knowledgeGraph": {
    "url": "https://yoursite.com/knowledge-graph.json"
  }
}
```

---

### ❌ Wrong: Invalid timestamps
```json
{
  "generatedAt": "2025-11-02 12:00:00"
}
```

### ✅ Right: ISO 8601 format
```json
{
  "generatedAt": "2025-11-02T12:00:00Z"
}
```

---

## Getting Help

- **Specification:** https://github.com/pressonify/ai-discovery-protocol
- **Discussion Forum:** https://github.com/pressonify/ai-discovery-protocol/discussions
- **Issues:** https://github.com/pressonify/ai-discovery-protocol/issues
- **Email:** ai-discovery@pressonify.ai

---

## Next Steps

1. ✅ Implement Level 1 or Level 2 (today)
2. 📝 Submit your site to our directory: https://pressonify.ai/adp-directory
3. 🐦 Share on Twitter/X with hashtag #AIDiscoveryProtocol
4. ⭐ Star the GitHub repo: https://github.com/pressonify/ai-discovery-protocol

---

**Good luck! Your website is about to become discoverable to AI systems worldwide.** 🚀
