# Level 1: Minimal Implementation (15 minutes)

This is the absolute minimum implementation of the AI Discovery Protocol. Perfect for testing or quick proof-of-concept.

## What You're Creating

**Just 1 file:** `/ai-discovery.json` (20 lines)

## Time Required

⏱️ **15 minutes** (including upload and testing)

## Who This Is For

- Testing ADP before full commitment
- Static websites with infrequent updates
- Personal blogs, portfolios, small business sites
- "I just want to try this" approach

## Step-by-Step Implementation

### Step 1: Copy the Template (2 minutes)

Copy [ai-discovery.json](ai-discovery.json) from this directory.

### Step 2: Customize (5 minutes)

Replace these placeholders with your information:

```json
{
  "website": {
    "url": "https://example.com",          ← Your domain
    "name": "Example Corporation",         ← Your company/site name
    "description": "Brief description..."  ← 1-2 sentence summary
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://example.com/knowledge-graph.json"  ← Update domain
    }
  }
}
```

**Example (fictional e-commerce store):**
```json
{
  "$schema": "https://pressonify.ai/schemas/ai-discovery/v1.0.json",
  "version": "1.0.0",
  "generatedAt": "2025-11-05T14:30:00Z",
  "website": {
    "url": "https://myhandmadecandles.com",
    "name": "Eco Candles Ireland",
    "description": "Handcrafted eco-friendly soy candles made in Dublin, Ireland"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://myhandmadecandles.com/knowledge-graph.json",
      "format": "application/ld+json"
    }
  }
}
```

### Step 3: Update Timestamp (1 minute)

Set `generatedAt` to current time in RFC 3339 format:

**Get current timestamp:**
```bash
# Mac/Linux
date -u +"%Y-%m-%dT%H:%M:%SZ"

# Output: 2025-11-05T14:30:00Z
```

Or use: https://timestamp.online

### Step 4: Upload to Your Website (5 minutes)

**Option A: FTP/SFTP**
```
Upload ai-discovery.json to your website root:
/public_html/ai-discovery.json
or
/var/www/html/ai-discovery.json
```

**Option B: CMS (WordPress, Joomla, etc.)**
1. Go to your file manager
2. Navigate to root directory
3. Upload ai-discovery.json

**Option C: Static Site Generator (Gatsby, Hugo, Next.js)**
```bash
# Copy to public directory
cp ai-discovery.json /path/to/your/project/public/

# Rebuild and deploy
npm run build && npm run deploy
```

**Option D: Cloud Storage (S3, CloudFlare, etc.)**
```bash
# AWS S3 example
aws s3 cp ai-discovery.json s3://yourbucket/ --acl public-read
```

### Step 5: Test (2 minutes)

**Test 1: File accessibility**
```bash
curl https://yourdomain.com/ai-discovery.json
```

Should return your JSON file (not 404).

**Test 2: JSON validity**
```bash
curl https://yourdomain.com/ai-discovery.json | jq .
```

Should output formatted JSON (no syntax errors).

**Test 3: In browser**
```
https://yourdomain.com/ai-discovery.json
```

Should display JSON (or download file).

---

## What This Gives You

✅ **Basic AI discoverability** - AI systems can find your website
✅ **Single entry point** - ai-discovery.json maps future resources
✅ **Minimal maintenance** - Update only when adding endpoints
✅ **Foundation for growth** - Easy to upgrade to Level 2 later

❌ **Limitations of Level 1:**
- No structured entity catalog (knowledge graph)
- No human-readable context (llms.txt)
- No explicit AI crawler directives (robots.txt)
- Limited discoverability compared to Level 2

---

## Upgrade Path to Level 2

**When you're ready (recommend within 30 days):**

1. Create `knowledge-graph.json` - Catalog your entities (products, articles, etc.)
2. Create `llms.txt` - Human-readable context document
3. Update `robots.txt` - Add AI crawler directives
4. Update `ai-discovery.json` - Add new endpoints

**Time to upgrade:** 2-4 hours
**Guide:** See [../standard/](../standard/) for Level 2 templates

---

## Maintenance

### Monthly (5 minutes)
- Update `generatedAt` timestamp
- Verify file is still accessible

### When Adding Endpoints (10 minutes)
- Add new endpoints to `endpoints` object
- Update `generatedAt` timestamp

**Example (adding llms.txt):**
```json
{
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://example.com/knowledge-graph.json",
      "format": "application/ld+json"
    },
    "contextDocument": {
      "url": "https://example.com/llms.txt",
      "format": "text/markdown"
    }
  }
}
```

---

## Troubleshooting

### File returns 404 Not Found
**Problem:** File not in root directory
**Solution:** Ensure ai-discovery.json is at `https://yourdomain.com/ai-discovery.json` (not in /public/ or subdirectory)

### JSON syntax error
**Problem:** Invalid JSON formatting
**Solution:** Validate with `jq` or https://jsonlint.com/

### CORS errors
**Problem:** Missing CORS headers
**Solution:** Add to server config:
```nginx
location /ai-discovery.json {
  add_header Access-Control-Allow-Origin *;
}
```

### Content-Type is text/html instead of application/json
**Problem:** Server misconfiguration
**Solution:** Add to server config:
```nginx
location ~ \.json$ {
  add_header Content-Type application/json;
}
```

---

## Real-World Examples

### Personal Blog
```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-05T10:00:00Z",
  "website": {
    "url": "https://johndoe.com",
    "name": "John Doe - Tech Blog",
    "description": "Software engineering blog covering Python, JavaScript, and AI"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://johndoe.com/knowledge-graph.json",
      "format": "application/ld+json"
    }
  }
}
```

### E-commerce Store
```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-05T12:00:00Z",
  "website": {
    "url": "https://craftshop.ie",
    "name": "Irish Craft Shop",
    "description": "Handmade Irish crafts, pottery, and gifts shipped worldwide"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://craftshop.ie/knowledge-graph.json",
      "format": "application/ld+json"
    }
  }
}
```

### SaaS Platform
```json
{
  "version": "1.0.0",
  "generatedAt": "2025-11-05T15:30:00Z",
  "website": {
    "url": "https://projectmanager.io",
    "name": "ProjectManager.io",
    "description": "AI-powered project management software for remote teams"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://projectmanager.io/knowledge-graph.json",
      "format": "application/ld+json"
    }
  }
}
```

---

## Next Steps

1. ✅ **Deploy** - Upload ai-discovery.json to your domain root
2. ✅ **Test** - Verify file is accessible at https://yourdomain.com/ai-discovery.json
3. ⏰ **Schedule upgrade** - Plan to implement Level 2 within 30 days for full benefits
4. 📊 **Monitor** - Watch server logs for AI crawler visits (GPTBot, Claude-Web, PerplexityBot)

---

## Additional Resources

- **Level 2 (Standard):** [../standard/](../standard/) - Recommended upgrade path
- **Full Specification:** [../../SPECIFICATION.md](../../SPECIFICATION.md)
- **Quick Start Guide:** [../../QUICK_START.md](../../QUICK_START.md)
- **FAQ:** [../../FAQ.md](../../FAQ.md)

---

## Support

- **GitHub Issues:** https://github.com/BuddySpuds/AI-Discovery-Protocol/issues
- **Email:** ai-discovery@pressonify.ai

---

*AI Discovery Protocol v1.0 | Level 1: Minimal | 15-minute implementation*
