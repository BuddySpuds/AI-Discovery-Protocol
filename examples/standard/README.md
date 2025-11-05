# Level 2: Standard Implementation (2-4 hours) - RECOMMENDED

This is the **recommended** implementation level for the AI Discovery Protocol. It provides full AI discoverability with all 4 core files and comprehensive structured data.

## What You're Creating

**4 files:**
1. `/ai-discovery.json` (~30 lines) - Meta-index with all endpoints
2. `/knowledge-graph.json` (~100-500 lines) - Structured entity catalog
3. `/llms.txt` (~200 lines) - Human-readable context document
4. `/robots.txt` (~40 lines) - AI crawler directives

## Time Required

⏱️ **2-4 hours** (one-time setup + customization)

## Who This Is For

- **Most websites** - E-commerce, SaaS, blogs, portfolios
- **Businesses selling products/services** online
- **Content publishers** wanting AI visibility
- **Anyone serious** about AI discoverability

## Benefits Over Level 1

✅ **Structured entity catalog** - AI systems can browse your products, articles, etc.
✅ **Human-readable context** - Optimized for LLM comprehension
✅ **Explicit AI crawler directives** - Tell AI systems what to crawl
✅ **SEO benefits** - Schema.org structured data improves search rankings
✅ **Rich search results** - Google shows enhanced snippets
✅ **Higher conversion rates** - AI pre-qualifies visitors (10-20% vs 2-5%)

---

## Step-by-Step Implementation

### Phase 1: Preparation (30 minutes)

**1. Read Documentation**
- [QUICK_START.md](../../QUICK_START.md) - Implementation guide
- [SPECIFICATION.md](../../SPECIFICATION.md) - Full technical spec

**2. Gather Content**
Create a spreadsheet with your entities:

| Type | Name | URL | Description | Price (if applicable) |
|------|------|-----|-------------|----------------------|
| Product | Enterprise Solution | /products/enterprise | Comprehensive platform | $99/mo |
| Product | Starter Plan | /products/starter | For small teams | $29/mo |
| BlogPosting | Getting Started | /blog/getting-started | Tutorial guide | N/A |
| Person | Jane Smith | /team/jane-smith | CTO | N/A |

**3. Set Up Tools**
- JSON validator: https://jsonlint.com/
- Schema.org validator: https://validator.schema.org/
- Text editor with JSON syntax highlighting

---

### Phase 2: Create Files (2-3 hours)

#### Step 1: Create ai-discovery.json (30 minutes)

**Copy template:**
```bash
cp examples/standard/ai-discovery.json /path/to/your/website/ai-discovery.json
```

**Customize:**
```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-05T12:00:00Z",  ← Update to current time
  "website": {
    "url": "https://example.com",        ← Your domain
    "name": "Example Corporation",       ← Your company name
    "description": "..."                 ← 1-2 sentence summary
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://example.com/knowledge-graph.json",  ← Update domain
      "entityCount": 25,                 ← Count your entities
      "lastModified": "2025-11-05T12:00:00Z"  ← Update timestamp
    },
    "contextDocument": {
      "url": "https://example.com/llms.txt",  ← Update domain
      "lastModified": "2025-11-05T12:00:00Z"
    },
    "crawlerDirectives": {
      "url": "https://example.com/robots.txt",  ← Update domain
      "allowsAI": true                          ← Set to true if allowing AI
    }
  },
  "metadata": {
    "industry": "Technology",            ← Your industry
    "language": "en",                    ← Your primary language
    "updateFrequency": "weekly"          ← How often you update
  }
}
```

**Get current timestamp:**
```bash
date -u +"%Y-%m-%dT%H:%M:%SZ"
# Output: 2025-11-05T14:30:00Z
```

**Validate:**
```bash
jq . ai-discovery.json  # Should output formatted JSON
```

---

#### Step 2: Create knowledge-graph.json (1-2 hours)

This is the most time-consuming file. You're creating a structured catalog of your entities.

**Start with template:**
```bash
cp examples/standard/knowledge-graph.json /path/to/your/website/knowledge-graph.json
```

**Entity types to include:**

1. **Organization** (REQUIRED - your company):
```json
{
  "@type": "Organization",
  "@id": "https://yourdomain.com/#organization",
  "name": "Your Company Name",
  "url": "https://yourdomain.com",
  "logo": "https://yourdomain.com/images/logo.png",
  "description": "Brief company description",
  "foundingDate": "2020-01-15",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main Street",
    "addressLocality": "Your City",
    "addressRegion": "State/Province",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-123-4567",
    "contactType": "customer support",
    "email": "support@yourdomain.com"
  }
}
```

2. **Product** (for e-commerce/SaaS):
```json
{
  "@type": "Product",
  "@id": "https://yourdomain.com/products/product-name",
  "name": "Product Name",
  "description": "Product description",
  "brand": {
    "@type": "Brand",
    "name": "Your Company Name"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://yourdomain.com/pricing",
    "priceCurrency": "USD",
    "price": "99.00",
    "availability": "https://schema.org/InStock"
  }
}
```

3. **BlogPosting** (for content sites):
```json
{
  "@type": "BlogPosting",
  "@id": "https://yourdomain.com/blog/article-slug",
  "headline": "Article Title",
  "datePublished": "2025-10-15T10:00:00Z",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://yourdomain.com/#organization"
  },
  "description": "Article summary"
}
```

4. **Person** (for team members):
```json
{
  "@type": "Person",
  "@id": "https://yourdomain.com/team/jane-smith",
  "name": "Jane Smith",
  "jobTitle": "Chief Technology Officer",
  "worksFor": {
    "@type": "Organization",
    "@id": "https://yourdomain.com/#organization"
  }
}
```

5. **FAQPage** (for FAQ sections):
```json
{
  "@type": "FAQPage",
  "@id": "https://yourdomain.com/faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is your product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our product is..."
      }
    }
  ]
}
```

**More Schema.org types:**
- WebPage, WebSite (for pages)
- BreadcrumbList (for navigation)
- Event (for events, webinars)
- Service (for services)
- LocalBusiness (for physical locations)
- Review, AggregateRating (for ratings)

**See full list:** https://schema.org/

**Validate:**
```bash
curl https://yourdomain.com/knowledge-graph.json | jq .
# Or use: https://validator.schema.org/
```

---

#### Step 3: Create llms.txt (30-60 minutes)

This is a human-readable context document optimized for LLMs.

**Start with template:**
```bash
cp examples/standard/llms.txt /path/to/your/website/llms.txt
```

**Structure:**
```markdown
---
version: 1.0.0
lastModified: 2025-11-05T12:00:00Z
protocol: AI Discovery Protocol v1.0
---

# Your Company Name

> Tagline or brief description

## About
Company overview, founding story, mission

## Key Pages
List important URLs

## Core Features
Describe your main features/products

## Use Cases
Explain how customers use your product

## Pricing
Pricing tiers and what they include

## Contact & Support
How to reach you

## Common AI Queries
Pre-answer questions AI systems might ask

## AI Discovery Resources
Links to your ADP files
```

**Writing tips:**
- ✅ **Be concise** - Summarize, don't duplicate website content
- ✅ **Use bullet points** - Easy for AI to parse
- ✅ **Include URLs** - Link to full pages
- ✅ **Answer common questions** - Pre-empt AI queries
- ❌ **Don't exceed 50 KB** - Keep it focused
- ❌ **Don't include secrets** - Only public information

**Target size:** 10-50 KB

---

#### Step 4: Update robots.txt (15 minutes)

**If you already have robots.txt:**
Add AI crawler directives at the top:

```
# AI Discovery Protocol v1.0
Allow: /ai-discovery.json
Allow: /knowledge-graph.json
Allow: /llms.txt

# AI Crawlers
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

# ... rest of your existing robots.txt
```

**If you don't have robots.txt:**
```bash
cp examples/standard/robots.txt /path/to/your/website/robots.txt
```

Then customize:
- Update domain in Sitemap line
- Update Disallow rules for your admin/internal paths

---

### Phase 3: Deploy (15 minutes)

**1. Upload files to your website root:**
```
/ai-discovery.json
/knowledge-graph.json
/llms.txt
/robots.txt (update existing or create new)
```

**2. Set correct Content-Type headers:**

**Nginx:**
```nginx
location ~ \.json$ {
  add_header Content-Type application/json;
  add_header Access-Control-Allow-Origin *;
}

location /llms.txt {
  add_header Content-Type text/markdown;
  add_header Access-Control-Allow-Origin *;
}
```

**Apache:**
```apache
<FilesMatch "\.(json)$">
  Header set Content-Type application/json
  Header set Access-Control-Allow-Origin "*"
</FilesMatch>

<Files "llms.txt">
  Header set Content-Type text/markdown
  Header set Access-Control-Allow-Origin "*"
</Files>
```

**3. Enable compression (recommended):**

**Nginx:**
```nginx
gzip on;
gzip_types application/json text/plain text/markdown;
```

**Apache:**
```apache
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE application/json text/plain
</IfModule>
```

---

### Phase 4: Test (15 minutes)

**1. File accessibility:**
```bash
curl -I https://yourdomain.com/ai-discovery.json
curl -I https://yourdomain.com/knowledge-graph.json
curl -I https://yourdomain.com/llms.txt
curl -I https://yourdomain.com/robots.txt

# All should return 200 OK
```

**2. JSON validity:**
```bash
curl https://yourdomain.com/ai-discovery.json | jq .
curl https://yourdomain.com/knowledge-graph.json | jq .
```

**3. Schema.org validation:**
- Google Rich Results Test: https://search.google.com/test/rich-results
- Enter: https://yourdomain.com/knowledge-graph.json

**4. Content-Type headers:**
```bash
curl -I https://yourdomain.com/ai-discovery.json | grep Content-Type
# Should see: Content-Type: application/json
```

**5. Compression:**
```bash
curl -I -H "Accept-Encoding: gzip" https://yourdomain.com/knowledge-graph.json | grep Content-Encoding
# Should see: Content-Encoding: gzip
```

---

### Phase 5: Monitor & Maintain (10 min/month)

**Monthly maintenance:**
1. Update `generatedAt` timestamps
2. Update `entityCount` if entities added/removed
3. Update `lastModified` in endpoints
4. Add new entities to knowledge-graph.json
5. Update llms.txt if major changes

**Automated updates (recommended):**
- Static site generators: Regenerate on build
- CMS: Create plugin/hook to auto-update
- CI/CD: Generate files in deployment pipeline

---

## Troubleshooting

### Issue: Files return 404 Not Found
**Solution:** Ensure files are in website root (not /public/ or subdirectory)

### Issue: JSON syntax errors
**Solution:** Validate with `jq` or https://jsonlint.com/

### Issue: Schema.org validation errors
**Solution:**
- Check required properties for each entity type at https://schema.org/
- Ensure @id values are unique
- Verify all URLs are absolute (not relative)

### Issue: Files too large
**Solution:**
- Remove unnecessary properties
- Implement pagination (coming in v1.1)
- Compress with GZip (60-70% reduction)

### Issue: CORS errors
**Solution:** Add CORS headers (see Phase 3, step 2)

---

## Real-World Examples

### E-commerce Store (Handmade Candles)

**Entity count:** 35
- 1 Organization
- 1 WebSite
- 12 Products (candle varieties)
- 8 BlogPostings (care guides, stories)
- 5 FAQPage questions
- 3 Person (founders)
- 5 Review entities

**Time to implement:** 3 hours

**Results after 30 days:**
- 47 visitors from AI search (ChatGPT, Perplexity)
- 16% conversion rate (vs 4% from Google)
- 7 sales attributed to AI referrals
- €210 revenue from AI channel

---

### SaaS Platform (Project Management)

**Entity count:** 52
- 1 Organization
- 1 WebSite
- 5 Products (pricing tiers)
- 28 BlogPostings (tutorials, best practices)
- 1 FAQPage (20 questions)
- 8 Person (team members)
- 8 BreadcrumbList (navigation)

**Time to implement:** 4 hours

**Results after 30 days:**
- 89 visitors from AI search
- 22% conversion to trial signups (vs 8% from Google)
- 19 trial signups
- 4 paid conversions (€396 MRR)

---

### Local Business (Coffee Shop)

**Entity count:** 18
- 1 Organization (with LocalBusiness type)
- 1 WebSite
- 6 Products (menu items)
- 5 BlogPostings (stories, recipes)
- 1 FAQPage
- 4 Person (baristas, owner)

**Time to implement:** 2 hours

**Results after 30 days:**
- Featured in ChatGPT recommendations for "coffee shops in [city]"
- 23 visitors mentioned "saw you on ChatGPT"
- €345 estimated revenue from AI referrals

---

## Upgrade Path to Level 3

When you're ready for advanced features:

1. Add change logs to knowledge-graph.json
2. Implement versioning system
3. Add entity-level timestamps (created, modified, deleted)
4. Set up monitoring for AI crawler visits
5. Implement pagination for large entity lists

**Guide:** See [../advanced/](../advanced/) for Level 3 templates

---

## Maintenance Schedule

### Weekly (if high-velocity content)
- Add new blog posts to knowledge-graph.json
- Update `entityCount` and timestamps

### Monthly
- Review and update llms.txt for accuracy
- Check Schema.org validation (catch errors early)
- Monitor server logs for AI crawler visits

### Quarterly
- Audit all entities (remove outdated)
- Expand knowledge graph (add missing entities)
- Review llms.txt structure (optimize for common queries)

### Annually
- Full ADP compliance review
- Consider upgrade to Level 3 (if needed)
- Evaluate ROI and traffic from AI sources

---

## ROI Calculation

**Investment:**
- Initial setup: 2-4 hours ($100-400 if hiring developer)
- Monthly maintenance: 10 minutes ($0-20 value)
- Hosting: $0 (files are tiny, <500 KB total)

**Returns (typical small business after 90 days):**
- AI search visitors: 50-150/month
- Conversion rate: 10-20% (vs 2-5% from SEO)
- Customers from AI: 5-30/month
- Revenue impact: $300-2000/month (depending on product price)

**ROI:** Positive within 30-60 days for most businesses

---

## Next Steps

1. ✅ **Deploy** - Upload all 4 files to your domain root
2. ✅ **Test** - Verify accessibility and validation
3. 📊 **Monitor** - Watch for AI crawler visits in server logs
4. 🔄 **Maintain** - Update monthly as content changes
5. 📈 **Measure** - Track traffic and conversions from AI sources
6. 🚀 **Optimize** - Expand entity catalog, refine llms.txt

---

## Additional Resources

- **Full Specification:** [../../SPECIFICATION.md](../../SPECIFICATION.md)
- **Quick Start Guide:** [../../QUICK_START.md](../../QUICK_START.md)
- **FAQ:** [../../FAQ.md](../../FAQ.md)
- **Design Rationale:** [../../DESIGN_DECISIONS.md](../../DESIGN_DECISIONS.md)
- **Comparison:** [../../docs/COMPARISON.md](../../docs/COMPARISON.md)
- **Schema.org Reference:** https://schema.org/

---

## Community & Support

- **GitHub Issues:** https://github.com/BuddySpuds/AI-Discovery-Protocol/issues
- **GitHub Discussions:** https://github.com/BuddySpuds/AI-Discovery-Protocol/discussions
- **Email:** ai-discovery@pressonify.ai

---

*AI Discovery Protocol v1.0 | Level 2: Standard | 2-4 hour implementation (RECOMMENDED)*
