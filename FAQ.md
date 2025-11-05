# Frequently Asked Questions (FAQ)

## General Questions

### What is the AI Discovery Protocol (ADP)?

The AI Discovery Protocol is an open standard that makes websites discoverable to AI systems (ChatGPT, Claude, Perplexity, Gemini). It provides a structured, machine-readable way for AI assistants to understand your website's content, products, services, and entities.

Think of it as "SEO for AI" - just as sitemaps help Google crawl your site, ADP helps AI systems understand and recommend your business.

**Key features:**
- 4-file architecture (ai-discovery.json, knowledge-graph.json, llms.txt, robots.txt)
- Single entry point for AI systems
- Based on open standards (Schema.org, JSON-LD)
- Free and open source (MIT License)

---

### How is ADP different from Schema.org?

**Schema.org** provides vocabularies for structured data, but doesn't define a discovery protocol.

**ADP** builds ON TOP of Schema.org by adding:
1. **Discovery mechanism** - Single entry point (ai-discovery.json) that maps all resources
2. **Freshness signals** - Timestamps, entity counts, change logs
3. **AI-optimized context** - llms.txt with human-readable Markdown
4. **Explicit AI crawler directives** - robots.txt with Allow statements

**Comparison:**
```
Schema.org alone:
  ✅ Structured data vocabularies
  ❌ No discovery mechanism
  ❌ No freshness signals
  ❌ AI systems must crawl entire site

ADP (with Schema.org):
  ✅ Structured data (via Schema.org)
  ✅ Single entry point (ai-discovery.json)
  ✅ Real-time freshness (timestamps, entity counts)
  ✅ AI finds everything in one request
```

**Bottom line:** Use Schema.org for your data, use ADP to make it discoverable.

---

### How is ADP different from llms.txt?

**llms.txt** (standalone) is just a Markdown file with context about your site.

**ADP** includes llms.txt as one component of a larger system:

| Feature | llms.txt alone | ADP (includes llms.txt) |
|---------|---------------|------------------------|
| Discovery | Manual (AI must guess filename) | Automatic (mapped in ai-discovery.json) |
| Structured data | None | Full knowledge graph (Schema.org) |
| Freshness signals | None | Timestamps, entity counts, change logs |
| Versioning | None | Semantic versioning built-in |
| AI crawler directives | None | robots.txt with explicit Allow rules |

**Bottom line:** llms.txt is great for context, but ADP provides the full discovery infrastructure.

---

### Do I still need traditional SEO?

**YES!** ADP complements traditional SEO, it doesn't replace it.

**Traditional SEO** (still critical):
- Google rankings (billions of searches)
- Backlinks, domain authority
- Content marketing, blog posts
- Meta tags, page speed

**ADP** (new opportunity):
- AI search visibility (ChatGPT, Claude, Perplexity)
- Structured entity catalog
- Faster discovery (6-24 hours vs 7-14 days)
- AI recommendations

**Best strategy:** Do both.
- Keep your SEO efforts (content, backlinks, optimization)
- Add ADP on top (30 minutes for minimal, 2-4 hours for standard)

**ROI:** ADP takes 30 minutes to implement and opens a new discovery channel. Traditional SEO takes months but reaches billions of users. Both are valuable.

---

### Will AI platforms actually use this?

**Current status:** ADP is a new standard (v1.0 released November 2025). AI platforms haven't officially adopted it yet.

**Why it's valuable anyway:**

1. **First-mover advantage:** Early adopters get visibility before competitors
2. **Based on standards:** Uses Schema.org (already widely supported)
3. **Structured data is useful:** Even if AI platforms don't use ADP directly, having structured data helps AI systems understand your site
4. **Signaling intent:** Explicitly telling AI systems "I want to be discoverable"

**What we know:**
- ✅ OpenAI (ChatGPT) crawls with GPTBot
- ✅ Anthropic (Claude) crawls with Claude-Web
- ✅ Perplexity crawls with PerplexityBot
- ✅ Google (Gemini) crawls with Google-Extended
- ⏳ None have officially adopted ADP (yet)

**Strategy:**
- **Conservative:** Wait for official adoption
- **Opportunistic:** Implement now, gain early visibility
- **Pragmatic:** Implement Level 1 (15 minutes), upgrade if adoption happens

**Worst case:** You spent 30 minutes and have structured data (useful for other purposes).

**Best case:** You're featured in AI recommendations before competitors catch on.

---

### What's the minimum implementation?

**Level 1 (Minimal) - 15 minutes:**

Just create `/ai-discovery.json` at your domain root:

```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-05T12:00:00Z",
  "website": {
    "url": "https://yourdomain.com",
    "name": "Your Company Name"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://yourdomain.com/knowledge-graph.json",
      "format": "application/ld+json"
    }
  }
}
```

That's it. 15 lines of JSON.

**Recommendation:** Invest 2-4 hours in Level 2 (Standard) for full benefits.

See [QUICK_START.md](QUICK_START.md) for detailed implementation guides.

---

### How long does implementation take?

| Level | Time | Files | Features |
|-------|------|-------|----------|
| **Level 1 (Minimal)** | 15 minutes | 1 file | Basic discovery |
| **Level 2 (Standard)** | 2-4 hours | 4 files | Full discovery (RECOMMENDED) |
| **Level 3 (Advanced)** | 1-2 days | 4 files + versioning | Change tracking, monitoring |

**Level 2 breakdown (2-4 hours):**
- 30 min: Create ai-discovery.json
- 60-90 min: Create knowledge-graph.json (catalog entities)
- 30-60 min: Create llms.txt (summarize your site)
- 15 min: Update robots.txt (add AI crawler directives)

**Faster with automation:**
- Static site generators (Gatsby, Hugo, Next.js): 30-60 min
- WordPress plugin (planned): 5 min
- Shopify app (planned): 5 min

---

### What's the ROI?

**Investment:**
- Time: 15 minutes (minimal) to 4 hours (standard)
- Cost: $0 (free and open source)
- Risk: Zero (just adding files)

**Return:**
- Be discoverable to 200M+ AI assistant users (ChatGPT alone has 200M weekly users)
- Higher conversion rates (10-20% vs 2-5% for SEO traffic, because AI pre-qualifies)
- First-mover advantage (6-12 month window before everyone does it)
- Future-proof as AI search grows

**Example scenario (small e-commerce store):**
```
Traditional SEO:
  - Investment: €900/month (content, links, tools)
  - Results: 200 visitors/month after 6 months
  - Conversion: 3% → 6 customers/month
  - Revenue: €300/month
  - ROI: Negative for 6+ months

ADP:
  - Investment: €0 (DIY) or €29/month (hosted)
  - Results: 50 visitors/month after 1 month (smaller but qualified)
  - Conversion: 15% → 7-8 customers/month
  - Revenue: €350-400/month
  - ROI: Positive from month 1
```

**Best strategy:** Do both (SEO for scale, ADP for early AI visibility).

See [docs/COMPARISON.md](docs/COMPARISON.md) for detailed ROI analysis.

---

### Who should implement this?

**Implement NOW if:**
- ✅ You sell products/services online
- ✅ You want early-adopter advantage
- ✅ You have 30 minutes (or a developer)
- ✅ You're tired of being invisible to AI search
- ✅ You want to be featured in ChatGPT/Claude results

**Good use cases:**
- E-commerce sites (product discovery)
- SaaS companies (feature documentation, brand awareness)
- Publishers (content discovery, author attribution)
- Local businesses (AI recommendations)
- B2B companies (thought leadership, case studies)
- Any website wanting visibility in AI search

**Skip for now if:**
- ❌ You don't have a website
- ❌ You're not selling anything online
- ❌ You don't care about AI search visibility

---

### Is this a standard or just a Pressonify thing?

**ADP is an open standard (MIT License), not proprietary to Pressonify.**

**Facts:**
- ✅ Open source (MIT License - free to use, modify, distribute)
- ✅ Public GitHub repository: https://github.com/BuddySpuds/AI-Discovery-Protocol
- ✅ Based on W3C standards (Schema.org, JSON-LD)
- ✅ Community contributions welcome
- ✅ Pressonify.ai is the *reference implementation*, not the owner

**Pressonify's role:**
- Created the specification (v1.0)
- First platform to implement it (live production example)
- Maintains the GitHub repository
- Welcomes community feedback and contributions

**Anyone can:**
- Implement ADP on their website (free)
- Build tools around it (validators, generators, plugins)
- Propose improvements (GitHub Issues/Discussions)
- Contribute implementations (WordPress, Shopify, Drupal, etc.)

**Goal:** Make this a community-driven standard, not a company-controlled protocol.

---

## Technical Questions

### What file sizes should I aim for?

**Recommended limits:**

| File | Target Size | Maximum Size | Notes |
|------|------------|--------------|-------|
| ai-discovery.json | < 5 KB | < 50 KB | Keep minimal (meta-index only) |
| knowledge-graph.json | < 200 KB | < 2 MB | Paginate if >10,000 entities |
| llms.txt | < 50 KB | < 500 KB | Summarize, don't duplicate content |
| robots.txt | < 10 KB | < 100 KB | Standard size |

**Why limits matter:**
- AI systems may timeout on large files
- Network latency impacts discovery speed
- Caching is less effective for large files

**If you exceed limits:**
- **knowledge-graph.json > 2 MB:** Implement pagination (planned v1.1)
- **llms.txt > 500 KB:** Split into sections, prioritize high-value content

---

### Should I compress the files?

**YES - Enable GZip compression on your server.**

**Example (Apache):**
```apache
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE application/json
  AddOutputFilterByType DEFLATE text/plain
</IfModule>
```

**Example (Nginx):**
```nginx
gzip on;
gzip_types application/json text/plain;
```

**Impact:**
- Typical compression: 60-70% size reduction
- Example: 150 KB → 45 KB
- Faster downloads for AI systems

**Pressonify reference implementation:**
- Compression ratio: 68%
- Average load time: 0.592s

---

### How often should I update the files?

**Update frequency depends on content velocity:**

| Content Type | Update Frequency | Example |
|--------------|-----------------|---------|
| Static sites | Monthly | Brochure websites, portfolios |
| Blogs | Weekly | New blog posts |
| E-commerce | Daily | Product launches, price changes |
| News sites | Hourly | Breaking news |
| Real-time | On-demand | User-generated content |

**Minimum requirements:**
- Update `generatedAt` timestamp every time
- Update `entityCount` if adding/removing entities
- Add change logs for Level 3 (Advanced) implementations

**Pro tip:** Automate updates via CI/CD or CMS hooks.

---

### What about Schema.org validation?

**Use existing validators:**

1. **Google Rich Results Test**
   - URL: https://search.google.com/test/rich-results
   - Tests: JSON-LD syntax, Schema.org compliance

2. **Schema.org Validator**
   - URL: https://validator.schema.org/
   - Tests: Full Schema.org validation

3. **JSON-LD Playground**
   - URL: https://json-ld.org/playground/
   - Tests: JSON-LD syntax, expansion

**For knowledge-graph.json:**
```bash
# Extract @graph array and validate each entity
curl https://yourdomain.com/knowledge-graph.json | \
  jq '.["@graph"][]' | \
  curl -X POST https://validator.schema.org/ -d @-
```

**Validation tools (planned v1.1):**
- Python validator (pip install adp-validator)
- JavaScript validator (npm install adp-validator)
- CLI tool (adp validate https://yourdomain.com)

---

### How do I test if AI systems are discovering my site?

**Testing methods:**

1. **Direct file access:**
   ```bash
   curl https://yourdomain.com/ai-discovery.json
   curl https://yourdomain.com/knowledge-graph.json
   curl https://yourdomain.com/llms.txt
   ```

2. **robots.txt verification:**
   ```bash
   curl https://yourdomain.com/robots.txt | grep -A5 "GPTBot"
   ```

3. **HTTP headers:**
   ```bash
   curl -I https://yourdomain.com/ai-discovery.json
   # Should see: Content-Type: application/json
   # Should see: Last-Modified: [date]
   ```

4. **AI system testing (manual):**
   - Ask ChatGPT: "Find me [your product category] from [your domain]"
   - Ask Claude: "What does [your domain] offer?"
   - Ask Perplexity: "Tell me about [your company]"

5. **Server logs:**
   ```bash
   # Look for AI crawler user-agents
   tail -f /var/log/nginx/access.log | grep -E "GPTBot|Claude-Web|PerplexityBot"
   ```

**Expected timeline:**
- Files go live → 6-24 hours → AI systems discover your site

---

### Can I use this with a CDN?

**YES - CDNs are recommended for performance.**

**Configuration:**

1. **CloudFlare:**
   ```javascript
   // Cache ai-discovery.json for 1 hour
   addEventListener('fetch', event => {
     if (event.request.url.endsWith('/ai-discovery.json')) {
       event.respondWith(fetch(event.request, {
         cf: { cacheTtl: 3600 }
       }));
     }
   });
   ```

2. **AWS CloudFront:**
   ```json
   {
     "PathPattern": "/ai-discovery.json",
     "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6",
     "MinTTL": 3600,
     "MaxTTL": 86400
   }
   ```

**Cache durations:**
- ai-discovery.json: 1 hour (frequently updated)
- knowledge-graph.json: 1 hour (entity changes)
- llms.txt: 24 hours (stable content)
- robots.txt: 7 days (rarely changes)

**Important:**
- Set `Last-Modified` headers
- Use `ETag` for cache validation
- Enable CORS for cross-origin requests

---

## Implementation Questions

### I'm non-technical. Can I implement this myself?

**YES - Level 1 (Minimal) requires no technical skills.**

**Step-by-step (15 minutes):**

1. Copy the [minimal example](examples/minimal/ai-discovery.json)
2. Replace placeholders with your info:
   - Your website URL
   - Your company name
3. Upload to your website root (ask your hosting provider)
4. Test: https://yourdomain.com/ai-discovery.json

**If you can upload a file, you can implement ADP Level 1.**

**For Level 2 (Standard):**
- Consider hiring a developer (2-4 hours = $100-300)
- Or use automated tools (WordPress plugin, Shopify app - coming soon)

---

### What if my CMS doesn't allow root-level files?

**Workarounds:**

1. **WordPress:**
   - Use a plugin (coming soon)
   - Or upload via FTP to `/public_html/`

2. **Shopify:**
   - Use theme asset upload
   - Or use a Shopify app (coming soon)

3. **Wix, Squarespace (limited):**
   - Upload to `/public/` folder (if available)
   - Or use subdomain (e.g., api.yourdomain.com/ai-discovery.json)

4. **Static site generators:**
   - Add files to `/public/` or `/static/` folder
   - Auto-generate from site data (Gatsby, Hugo, Next.js)

5. **Headless CMS:**
   - Create API endpoint that returns JSON
   - Map to /ai-discovery.json via reverse proxy

**Worst case:** Host files on a subdomain (api.yourdomain.com) and use HTTP redirects.

---

### Should I auto-generate or hand-craft the files?

**Depends on your content velocity:**

| Scenario | Recommendation |
|----------|----------------|
| Static site (5-20 pages) | Hand-craft (one-time effort) |
| Blog (weekly posts) | Auto-generate via CMS hooks |
| E-commerce (daily changes) | Auto-generate via product feed |
| News site (hourly updates) | Auto-generate via CI/CD |

**Auto-generation benefits:**
- Always up-to-date
- No manual maintenance
- Scales to thousands of entities

**Hand-crafting benefits:**
- Full control over content
- Better optimization
- Good for small sites

**Best approach:** Start with hand-crafted templates, automate later if needed.

---

### Can I use this for a multi-language site?

**YES - Use hreflang-style language codes.**

**Approach 1: Separate files per language**
```
/en/ai-discovery.json
/es/ai-discovery.json
/fr/ai-discovery.json
```

**Approach 2: Language parameter (planned v1.1)**
```
/ai-discovery.json?lang=en
/ai-discovery.json?lang=es
```

**Approach 3: Single file with translations (not recommended)**
```json
{
  "website": {
    "name": {
      "en": "My Company",
      "es": "Mi Empresa",
      "fr": "Ma Société"
    }
  }
}
```

**Recommendation:** Use separate files (Approach 1) for better caching and clarity.

**Future support (v1.1):**
- Official multi-language guidelines
- `language` field in ai-discovery.json
- Localized examples

---

## Security & Privacy

### What data should I include?

**Safe to include:**
- ✅ Public content (already on your website)
- ✅ Product information (names, prices, descriptions)
- ✅ Blog posts, articles, press releases
- ✅ Company info (name, description, location)
- ✅ Public contact info (support email, phone)

**DO NOT include:**
- ❌ User data (customer names, emails, orders)
- ❌ Private content (draft posts, internal docs)
- ❌ API keys, passwords, secrets
- ❌ Personally identifiable information (PII)
- ❌ Financial data (credit cards, bank accounts)

**Rule of thumb:** If it's not already public on your website, don't include it in ADP files.

---

### Should I rate-limit requests to these files?

**YES - Implement reasonable rate limits.**

**Recommended limits:**
- 60 requests/minute per IP (allows AI crawlers to fetch all 4 files)
- 1000 requests/day per IP (prevents abuse)

**Implementation (Nginx):**
```nginx
limit_req_zone $binary_remote_addr zone=adp:10m rate=60r/m;

location ~ ^/(ai-discovery\.json|knowledge-graph\.json|llms\.txt)$ {
  limit_req zone=adp burst=10 nodelay;
}
```

**Why rate limiting:**
- Prevents DDoS attacks
- Protects server resources
- Legitimate AI crawlers respect rate limits

**Don't over-restrict:** AI systems need to fetch files periodically. 60/min is generous.

---

### What about CORS headers?

**Enable CORS for cross-origin AI system requests.**

**Configuration (Nginx):**
```nginx
location ~ ^/(ai-discovery\.json|knowledge-graph\.json|llms\.txt)$ {
  add_header Access-Control-Allow-Origin *;
  add_header Access-Control-Allow-Methods "GET, OPTIONS";
}
```

**Configuration (Apache):**
```apache
<FilesMatch "\.(json|txt)$">
  Header set Access-Control-Allow-Origin "*"
  Header set Access-Control-Allow-Methods "GET, OPTIONS"
</FilesMatch>
```

**Why CORS:**
- AI systems may fetch files from client-side JavaScript
- Cross-origin requests fail without CORS headers
- Publicly accessible files should allow cross-origin access

---

## Roadmap & Future

### What's planned for v1.1?

**Planned features (Q1 2026):**
- Entity pagination for large knowledge graphs (>10,000 entities)
- Real-time updates via WebSocket endpoint
- Multi-language support and localization
- Official JSON Schema validation files
- Validation tools (Python, JavaScript, CLI)
- Additional platform implementations (WordPress, Drupal, Shopify)

See [CHANGELOG.md](CHANGELOG.md) for detailed roadmap.

---

### Can I contribute?

**YES! Contributions welcome.**

**Ways to contribute:**
1. **Report issues:** GitHub Issues
2. **Propose improvements:** GitHub Discussions
3. **Share implementations:** WordPress plugins, Shopify apps, etc.
4. **Improve docs:** Fix typos, add examples, translations
5. **Build tools:** Validators, generators, browser extensions

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

### How do I stay updated?

**Stay informed:**
- ⭐ Star the GitHub repo: https://github.com/BuddySpuds/AI-Discovery-Protocol
- 👀 Watch for releases (GitHub notifications)
- 💬 Join discussions: GitHub Discussions
- 📧 Email: ai-discovery@pressonify.ai
- 🐦 Twitter: @PressonifyAI (coming soon)

**Release schedule:**
- v1.0: November 2025 (current)
- v1.1: Q1 2026 (planned)
- v2.0: Q3 2026 (under consideration)

---

## Getting Help

### Where can I find examples?

**In this repository:**
- [examples/minimal/](examples/minimal/) - 15-minute implementation
- [examples/standard/](examples/standard/) - 2-4 hour implementation (RECOMMENDED)
- [examples/advanced/](examples/advanced/) - 1-2 day implementation with versioning
- [examples/press-release-platform/](examples/press-release-platform/) - Pressonify.ai reference

**Live production example:**
- Pressonify.ai: https://pressonify.ai/ai-discovery.json

---

### I'm stuck. How do I get support?

**Support channels:**

1. **Documentation:**
   - [README.md](README.md) - Technical overview
   - [SPECIFICATION.md](SPECIFICATION.md) - Full spec (13,500 words)
   - [QUICK_START.md](QUICK_START.md) - Step-by-step guides
   - [docs/EXPLAINED_SIMPLY.md](docs/EXPLAINED_SIMPLY.md) - Layperson explanation

2. **Community:**
   - GitHub Discussions: https://github.com/BuddySpuds/AI-Discovery-Protocol/discussions
   - GitHub Issues: https://github.com/BuddySpuds/AI-Discovery-Protocol/issues

3. **Direct support:**
   - Email: ai-discovery@pressonify.ai
   - Response time: 1-3 business days

---

### Can I hire someone to implement this?

**YES - Implementation services:**

1. **Freelancers:**
   - Upwork, Fiverr (search "AI Discovery Protocol implementation")
   - Budget: $100-300 for Level 2 (Standard)

2. **Agencies:**
   - SEO agencies, web development firms
   - Budget: $500-2000 for Level 3 (Advanced) + custom features

3. **Pressonify (official):**
   - Automated implementation (coming soon)
   - Pricing: $29/month (hosted, auto-updates)

**DIY is recommended** for most sites - Level 2 takes 2-4 hours with our guides.

---

## Still have questions?

**Ask the community:**
- GitHub Discussions: https://github.com/BuddySpuds/AI-Discovery-Protocol/discussions
- Email: ai-discovery@pressonify.ai

**Contribute to this FAQ:**
- Submit a PR with your question + answer
- Or open an issue labeled "FAQ"

---

*AI Discovery Protocol v1.0 | November 2025 | Making websites discoverable to AI systems*
