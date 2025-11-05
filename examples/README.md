# AI Discovery Protocol - Implementation Examples

This directory contains working examples for all three implementation levels of the AI Discovery Protocol.

## Quick Navigation

| Level | Time Required | Files | Description | Directory |
|-------|--------------|-------|-------------|-----------|
| **Level 1 (Minimal)** | 15 minutes | 1 file | Basic discovery - just ai-discovery.json | [minimal/](minimal/) |
| **Level 2 (Standard)** | 2-4 hours | 4 files | Full discovery (RECOMMENDED) | [standard/](standard/) |
| **Level 3 (Advanced)** | 1-2 days | 4 files + versioning | Change tracking, monitoring | [advanced/](advanced/) |
| **Reference Implementation** | N/A | Live production | Pressonify.ai (real-world example) | [press-release-platform/](press-release-platform/) |

---

## Level 1: Minimal Implementation (15 minutes)

**Perfect for:**
- Testing ADP before full commitment
- Static websites with infrequent updates
- Quick proof-of-concept

**What you get:**
- Basic AI discoverability
- Single entry point (ai-discovery.json)
- Minimal maintenance

**What you create:**
```
/ai-discovery.json  (1 file, ~20 lines)
```

**See:** [minimal/](minimal/) for complete example

---

## Level 2: Standard Implementation (2-4 hours) - RECOMMENDED

**Perfect for:**
- Most websites and applications
- E-commerce stores
- Blogs and content sites
- SaaS platforms

**What you get:**
- Full AI discoverability
- Structured entity catalog (knowledge graph)
- Human-readable context document
- AI crawler directives
- SEO benefits from structured data

**What you create:**
```
/ai-discovery.json       (~30 lines)
/knowledge-graph.json    (~100-500 lines, depending on entities)
/llms.txt                (~50-200 lines)
/robots.txt              (~20-30 lines for AI section)
```

**See:** [standard/](standard/) for complete templates

---

## Level 3: Advanced Implementation (1-2 days)

**Perfect for:**
- Large-scale platforms (>1000 entities)
- High-velocity content sites (daily updates)
- Enterprise applications
- When you need analytics and monitoring

**What you get:**
- Everything from Level 2
- Entity-level change tracking
- Version history
- Real-time freshness signals
- Analytics support

**What you create:**
```
/ai-discovery.json       (with all optional fields)
/knowledge-graph.json    (with changeLog per entity)
/llms.txt                (with version history)
/robots.txt              (complete configuration)
```

**See:** [advanced/](advanced/) for complete example

---

## Reference Implementation: Pressonify.ai

**Live production example:**
- Domain: https://pressonify.ai
- Platform: Press release distribution + AI optimization
- Scale: 17 entities (4 base + 13 NewsArticle entities)
- Performance: 0.592s average load time, 68% compression

**Live endpoints:**
- https://pressonify.ai/ai-discovery.json
- https://pressonify.ai/knowledge-graph.json
- https://pressonify.ai/llms.txt
- https://pressonify.ai/robots.txt

**See:** [press-release-platform/](press-release-platform/) for reference documentation

---

## Choosing Your Implementation Level

### Start with Level 1 if:
- ⏱️ You have 15 minutes right now
- 🧪 You want to test ADP before committing
- 📄 Your site has <10 pages
- 🔒 You're risk-averse (minimal investment)

**Then upgrade to Level 2 within 30 days** for full benefits.

---

### Start with Level 2 if:
- ✅ You're serious about AI discoverability
- 📦 You have products/services to catalog
- 📝 You publish content regularly
- 💼 You're a business (not just testing)
- ⚡ You have 2-4 hours to invest

**This is the RECOMMENDED starting point for most websites.**

---

### Start with Level 3 if:
- 🏢 You're an enterprise with >1000 entities
- 📊 You need analytics and tracking
- 🚀 You update content hourly/daily
- 👨‍💻 You have developer resources
- 📈 You want to monitor AI crawler behavior

**Warning:** Level 3 requires maintenance. Start with Level 2, upgrade later if needed.

---

## File Structure Overview

### ai-discovery.json (REQUIRED)

**Purpose:** Meta-index and single entry point for AI systems

**Size:** 1-5 KB (keep minimal)

**Key fields:**
```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-05T12:00:00Z",
  "website": {...},
  "endpoints": {...}
}
```

**Update frequency:** Whenever you add/remove endpoints or entities

---

### knowledge-graph.json (RECOMMENDED)

**Purpose:** Structured catalog of your entities (products, articles, people, etc.)

**Size:** 50 KB - 2 MB (paginate if larger)

**Format:** Schema.org JSON-LD with @graph array

**Key fields:**
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "name": "...",
      ...
    },
    {
      "@type": "Product",
      "name": "...",
      ...
    }
  ]
}
```

**Update frequency:** When entities change (products added/removed, content published)

---

### llms.txt (RECOMMENDED)

**Purpose:** Human-readable context document for AI systems

**Size:** 10-50 KB (summarize, don't duplicate)

**Format:** YAML frontmatter + Markdown

**Structure:**
```markdown
---
title: Company Name
lastUpdated: 2025-11-05
version: 1.0.0
---

# About

Brief description...

## Products & Services

- Product 1: Description
- Product 2: Description

## Use Cases

...
```

**Update frequency:** Monthly (or when major changes occur)

---

### robots.txt (STANDARD)

**Purpose:** Explicit AI crawler directives

**Size:** 1-10 KB

**AI section:**
```
User-agent: GPTBot
Allow: /
Allow: /ai-discovery.json
Allow: /knowledge-graph.json
Allow: /llms.txt

User-agent: Claude-Web
Allow: /
...
```

**Update frequency:** Rarely (only when adding new directives)

---

## Implementation Workflow

### Quick Start (Level 2 Standard)

**Phase 1: Preparation (30 minutes)**
1. Read [QUICK_START.md](../QUICK_START.md)
2. Review [standard/](standard/) templates
3. Gather your content (products, articles, company info)

**Phase 2: Create Files (2-3 hours)**
1. Copy [standard/ai-discovery.json](standard/ai-discovery.json) template
2. Copy [standard/knowledge-graph.json](standard/knowledge-graph.json) template
3. Copy [standard/llms.txt](standard/llms.txt) template
4. Update [standard/robots.txt](standard/robots.txt) template

**Phase 3: Customize (1 hour)**
1. Replace placeholders with your data
2. Catalog your entities (products, articles, etc.)
3. Write llms.txt context document
4. Update robots.txt with AI directives

**Phase 4: Deploy (15 minutes)**
1. Upload files to your domain root
2. Test: `curl https://yourdomain.com/ai-discovery.json`
3. Validate Schema.org: https://validator.schema.org/
4. Monitor server logs for AI crawlers

**Phase 5: Maintain (10 min/month)**
1. Update `generatedAt` timestamps
2. Add new entities to knowledge graph
3. Update `entityCount` in ai-discovery.json
4. Keep llms.txt current

---

## Testing Your Implementation

### 1. File Accessibility
```bash
# Test all 4 files
curl -I https://yourdomain.com/ai-discovery.json
curl -I https://yourdomain.com/knowledge-graph.json
curl -I https://yourdomain.com/llms.txt
curl -I https://yourdomain.com/robots.txt

# Should return 200 OK with correct Content-Type
```

### 2. JSON Validation
```bash
# Validate JSON syntax
curl https://yourdomain.com/ai-discovery.json | jq .
curl https://yourdomain.com/knowledge-graph.json | jq .
```

### 3. Schema.org Validation
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org/

### 4. AI Crawler Discovery
```bash
# Monitor server logs
tail -f /var/log/nginx/access.log | grep -E "GPTBot|Claude-Web|PerplexityBot"
```

### 5. Manual AI Testing
- Ask ChatGPT: "Find me [your product] from [your domain]"
- Ask Claude: "What does [your domain] offer?"
- Ask Perplexity: "Tell me about [your company]"

---

## Common Issues & Solutions

### Issue: Files return 404 Not Found
**Solution:** Ensure files are in your website's root directory (not /public/ or /static/)

### Issue: CORS errors in browser console
**Solution:** Add CORS headers to your server configuration:
```nginx
location ~ \.(json|txt)$ {
  add_header Access-Control-Allow-Origin *;
}
```

### Issue: JSON syntax errors
**Solution:** Use a JSON validator before deploying:
```bash
jq . ai-discovery.json  # Should output formatted JSON
```

### Issue: Schema.org validation errors
**Solution:** Check entity types and required properties at https://schema.org/

### Issue: Files too large (>2 MB)
**Solution:**
- Implement pagination (coming in v1.1)
- Remove unnecessary properties
- Compress with GZip (should get 60-70% reduction)

---

## Next Steps

1. **Choose your level:** Start with [minimal/](minimal/) to test, or [standard/](standard/) for full implementation
2. **Read guides:** See [QUICK_START.md](../QUICK_START.md) for detailed instructions
3. **Deploy:** Upload files to your domain root
4. **Test:** Use testing methods above
5. **Monitor:** Watch for AI crawler visits in server logs
6. **Iterate:** Update files as your content changes

---

## Additional Resources

- **Full Specification:** [SPECIFICATION.md](../SPECIFICATION.md)
- **Design Rationale:** [DESIGN_DECISIONS.md](../DESIGN_DECISIONS.md)
- **FAQ:** [FAQ.md](../FAQ.md)
- **Comparison:** [docs/COMPARISON.md](../docs/COMPARISON.md)
- **Layperson Guide:** [docs/EXPLAINED_SIMPLY.md](../docs/EXPLAINED_SIMPLY.md)

---

## Community & Support

- **GitHub Issues:** https://github.com/BuddySpuds/AI-Discovery-Protocol/issues
- **GitHub Discussions:** https://github.com/BuddySpuds/AI-Discovery-Protocol/discussions
- **Email:** ai-discovery@pressonify.ai

---

*AI Discovery Protocol v1.0 | November 2025 | Open Standard (MIT License)*
