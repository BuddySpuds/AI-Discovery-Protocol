# AI Discovery Protocol v2.0 Migration Guide

**From:** v1.0.0
**To:** v2.0
**Release Date:** December 2, 2025

---

## Overview

AI Discovery Protocol v2.0 introduces enhanced capabilities for optimization transparency and protocol feature declaration while maintaining backward compatibility with v1.0 implementations. This guide will help you migrate from v1.0.0 to v2.0.

---

## Breaking Changes

### 1. Version Pattern Format

**Changed:** Version field pattern from semantic versioning to major.minor format.

**v1.0 Format:**
```json
{
  "version": "1.0.0"
}
```

**v2.0 Format:**
```json
{
  "version": "2.0"
}
```

**Why:** Protocol versions track spec changes, not implementation versions. Simplified format (2.0, 2.1, 3.0) is more intuitive than semantic versioning (1.0.0, 1.0.1, 1.1.0).

**Migration:**
- Change `"version": "1.0.0"` to `"version": "2.0"`
- Update schema reference from `v1.0.json` to `v2.0.json`

---

### 2. Schema Reference Update

**Changed:** Schema URL must point to v2.0 schema.

**v1.0 Schema:**
```json
{
  "$schema": "https://pressonify.ai/schemas/ai-discovery/v1.0.json"
}
```

**v2.0 Schema:**
```json
{
  "$schema": "https://pressonify.ai/schemas/ai-discovery/v2.0.json"
}
```

**Migration:**
- Update `$schema` field to v2.0 URL
- Validate against v2.0 JSON Schema

---

### 3. Metadata Object Requirements

**Changed:** `metadata` object is now optional in v2.0 (was required in v1.0).

**v1.0 (Required):**
```json
{
  "metadata": {
    "language": "en",
    "updateFrequency": "daily"
  }
}
```

**v2.0 (Optional):**
```json
{
  "metadata": {
    "industry": "SaaS",
    "language": "en",
    "timezone": "UTC"
  }
}
```

**Why:** `updateFrequency` moved to `capabilities` object. Language and timezone are not critical for AI discovery.

**Migration:**
- Move `updateFrequency` from `metadata` to `capabilities.updateFrequency`
- Make `metadata` object optional (can be omitted if not needed)
- Remove `language` requirement (now truly optional)

---

## New Required Fields

### None

All new fields in v2.0 are **optional**. This ensures backward compatibility with v1.0 files.

---

## New Optional Fields

### 1. Capabilities Object (Recommended)

**Purpose:** Declare protocol feature support to AI systems.

**Structure:**
```json
{
  "capabilities": {
    "supportsVersioning": true,
    "supportsIncrementalUpdates": true,
    "supportsChangeDetection": true,
    "updateFrequency": "daily"
  }
}
```

**Fields:**
- `supportsVersioning` (boolean) — Does your knowledge graph use versioning?
- `supportsIncrementalUpdates` (boolean) — Can AI systems request only changed entities?
- `supportsChangeDetection` (boolean) — Do you provide change logs?
- `updateFrequency` (enum) — How often is content updated? (realtime, hourly, daily, weekly, monthly, quarterly, annually)

**Migration:**
1. Add `capabilities` object to your ai-discovery.json
2. Set feature flags based on your implementation
3. Move `updateFrequency` from `metadata` to `capabilities`

**Example:**
```json
{
  "version": "2.0",
  "capabilities": {
    "supportsVersioning": true,
    "supportsIncrementalUpdates": false,
    "supportsChangeDetection": false,
    "updateFrequency": "daily"
  }
}
```

---

### 2. Contact Object (Recommended)

**Purpose:** Provide support channels for ADP-related technical questions.

**Structure:**
```json
{
  "contact": {
    "email": "ai-discovery@yourdomain.com",
    "issuesUrl": "https://github.com/yourorg/ai-discovery/issues"
  }
}
```

**Fields:**
- `email` (string, format: email) — Email address for ADP inquiries
- `issuesUrl` (string, format: uri) — URL for reporting issues (GitHub, Jira, etc.)

**Migration:**
1. Decide on a support email address
2. Set up an issues tracker (GitHub Issues, Jira, etc.)
3. Add `contact` object to ai-discovery.json

**Example:**
```json
{
  "version": "2.0",
  "contact": {
    "email": "ai-discovery@pressonify.ai",
    "issuesUrl": "https://github.com/BuddySpuds/AI-Discovery-Protocol/issues"
  }
}
```

---

### 3. Enhanced Shopify Optimization Block (Shopify Users Only)

**Purpose:** Provide optimization transparency and distribution insights.

**v1.0 Structure (Deprecated):**
```json
{
  "shopify": {
    "optimizationStatus": {
      "totalOptimized": 342,
      "averageScore": 73.5
    }
  }
}
```

**v2.0 Structure (Enhanced):**
```json
{
  "shopify": {
    "optimization": {
      "version": "2.0",
      "scoringModel": "adp-v2.0-8factor",
      "distribution": {
        "fullyOptimized": 342,
        "partiallyOptimized": 89,
        "basic": 10
      },
      "baselineScoreRange": [35, 55],
      "averageScore": 73.5,
      "lastOptimized": "2025-12-02T14:30:00Z"
    }
  }
}
```

**New Fields:**
- `version` (string) — Optimization scoring model version
- `scoringModel` (string) — Name of scoring algorithm (e.g., "adp-v2.0-8factor")
- `distribution` (object) — Distribution of entities by optimization level
  - `fullyOptimized` (integer) — SEO score >= 70
  - `partiallyOptimized` (integer) — SEO score 45-69
  - `basic` (integer) — SEO score < 45
- `baselineScoreRange` (array[number, number]) — Dynamic baseline range [min, max]
- `averageScore` (number) — Average SEO score across all optimized entities
- `lastOptimized` (string, ISO 8601) — Timestamp of last optimization run

**Migration:**
1. Calculate optimization distribution across entities
2. Determine baseline score range for your content type
3. Replace `optimizationStatus` with `optimization` block
4. Keep `optimizationStatus` for backward compatibility (optional)

**Example:**
```json
{
  "shopify": {
    "entityCounts": {
      "products": 428,
      "collections": 12,
      "blogs": 8,
      "pages": 15
    },
    "optimization": {
      "version": "2.0",
      "scoringModel": "adp-v2.0-8factor",
      "distribution": {
        "fullyOptimized": 342,
        "partiallyOptimized": 89,
        "basic": 10
      },
      "baselineScoreRange": [35, 55],
      "averageScore": 73.5,
      "lastOptimized": "2025-12-02T14:30:00Z"
    }
  }
}
```

---

## Deprecations

### 1. shopify.optimizationStatus

**Status:** Deprecated in v2.0, will be removed in v3.0

**Replacement:** `shopify.optimization`

**Migration Path:**
1. Implement `shopify.optimization` block
2. Keep `optimizationStatus` for backward compatibility (optional)
3. Remove `optimizationStatus` when all consumers upgrade to v2.0+

**Backward Compatibility:**
Both fields can coexist during transition period:
```json
{
  "shopify": {
    "optimizationStatus": {
      "totalOptimized": 342,
      "averageScore": 73.5
    },
    "optimization": {
      "version": "2.0",
      "scoringModel": "adp-v2.0-8factor",
      "distribution": {
        "fullyOptimized": 342,
        "partiallyOptimized": 89,
        "basic": 10
      },
      "averageScore": 73.5,
      "lastOptimized": "2025-12-02T14:30:00Z"
    }
  }
}
```

---

## Step-by-Step Migration

### For Standard Implementations (Non-Shopify)

**1. Update Version Field**
```diff
- "version": "1.0.0"
+ "version": "2.0"
```

**2. Update Schema Reference**
```diff
- "$schema": "https://pressonify.ai/schemas/ai-discovery/v1.0.json"
+ "$schema": "https://pressonify.ai/schemas/ai-discovery/v2.0.json"
```

**3. Add Capabilities Object (Optional but Recommended)**
```json
{
  "capabilities": {
    "supportsVersioning": true,
    "supportsIncrementalUpdates": false,
    "supportsChangeDetection": false,
    "updateFrequency": "daily"
  }
}
```

**4. Add Contact Object (Optional but Recommended)**
```json
{
  "contact": {
    "email": "ai-discovery@yourdomain.com",
    "issuesUrl": "https://github.com/yourorg/issues"
  }
}
```

**5. Move updateFrequency from metadata to capabilities**
```diff
  "metadata": {
-   "language": "en",
-   "updateFrequency": "daily"
+   "language": "en"
  },
+ "capabilities": {
+   "updateFrequency": "daily"
+ }
```

**6. Validate Against v2.0 Schema**
```bash
# Using ajv-cli
ajv validate -s https://pressonify.ai/schemas/ai-discovery/v2.0.json -d ai-discovery.json
```

---

### For Shopify Implementations (PresSEO)

**Follow steps 1-6 above, then:**

**7. Calculate Optimization Distribution**
```javascript
// Example calculation
const fullyOptimized = entities.filter(e => e.seoScore >= 70).length;
const partiallyOptimized = entities.filter(e => e.seoScore >= 45 && e.seoScore < 70).length;
const basic = entities.filter(e => e.seoScore < 45).length;
```

**8. Add Optimization Block**
```json
{
  "shopify": {
    "optimization": {
      "version": "2.0",
      "scoringModel": "adp-v2.0-8factor",
      "distribution": {
        "fullyOptimized": 342,
        "partiallyOptimized": 89,
        "basic": 10
      },
      "baselineScoreRange": [35, 55],
      "averageScore": 73.5,
      "lastOptimized": "2025-12-02T14:30:00Z"
    }
  }
}
```

**9. (Optional) Keep optimizationStatus for Backward Compatibility**
```json
{
  "shopify": {
    "optimizationStatus": {
      "totalOptimized": 431,
      "averageScore": 73.5
    },
    "optimization": {
      "version": "2.0",
      "scoringModel": "adp-v2.0-8factor",
      "distribution": {
        "fullyOptimized": 342,
        "partiallyOptimized": 89,
        "basic": 10
      },
      "baselineScoreRange": [35, 55],
      "averageScore": 73.5,
      "lastOptimized": "2025-12-02T14:30:00Z"
    }
  }
}
```

---

## Code Examples

### Before (v1.0.0)

```json
{
  "$schema": "https://pressonify.ai/schemas/ai-discovery/v1.0.json",
  "version": "1.0.0",
  "generatedAt": "2025-11-05T12:00:00Z",
  "website": {
    "url": "https://example.com",
    "name": "Example Corp"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://example.com/knowledge-graph.json",
      "format": "application/ld+json",
      "entityCount": 150
    }
  },
  "metadata": {
    "language": "en",
    "updateFrequency": "daily"
  }
}
```

### After (v2.0)

```json
{
  "$schema": "https://pressonify.ai/schemas/ai-discovery/v2.0.json",
  "version": "2.0",
  "generatedAt": "2025-12-02T12:00:00Z",
  "website": {
    "url": "https://example.com",
    "name": "Example Corp"
  },
  "endpoints": {
    "knowledgeGraph": {
      "url": "https://example.com/knowledge-graph.json",
      "format": "application/ld+json",
      "entityCount": 150,
      "lastModified": "2025-12-02T11:00:00Z",
      "version": "2.0.1"
    }
  },
  "capabilities": {
    "supportsVersioning": true,
    "supportsIncrementalUpdates": false,
    "supportsChangeDetection": false,
    "updateFrequency": "daily"
  },
  "contact": {
    "email": "ai-discovery@example.com"
  },
  "metadata": {
    "language": "en",
    "timezone": "America/New_York"
  }
}
```

---

## Validation

### JSON Schema Validation

**v2.0 Schema URL:**
```
https://pressonify.ai/schemas/ai-discovery/v2.0.json
```

**Using ajv-cli:**
```bash
npm install -g ajv-cli
ajv validate \
  -s https://pressonify.ai/schemas/ai-discovery/v2.0.json \
  -d ai-discovery.json
```

**Using Python jsonschema:**
```python
import json
import requests
from jsonschema import validate

# Load schema
schema_url = "https://pressonify.ai/schemas/ai-discovery/v2.0.json"
schema = requests.get(schema_url).json()

# Load instance
with open("ai-discovery.json") as f:
    instance = json.load(f)

# Validate
validate(instance=instance, schema=schema)
print("✓ Valid ADP v2.0 file")
```

---

## Backward Compatibility

### v1.0 Files Still Work

AI Discovery Protocol v2.0 is **backward compatible** with v1.0 files:
- v1.0 files will continue to work with v2.0-aware AI systems
- New fields are **optional** (not breaking changes)
- Version field update is recommended but not enforced

### Gradual Migration Path

1. **Phase 1:** Update version field to "2.0" and schema reference
2. **Phase 2:** Add `capabilities` and `contact` objects
3. **Phase 3:** Migrate Shopify `optimizationStatus` to `optimization`
4. **Phase 4:** Remove deprecated fields (before v3.0)

---

## Testing Your Migration

### Checklist

- [ ] Version field updated to "2.0"
- [ ] Schema reference points to v2.0.json
- [ ] File validates against v2.0 JSON Schema
- [ ] `capabilities` object added (recommended)
- [ ] `contact` object added (recommended)
- [ ] `updateFrequency` moved from metadata to capabilities
- [ ] Shopify `optimization` block added (if applicable)
- [ ] Backward compatibility maintained (old consumers still work)
- [ ] HTTP headers unchanged (Content-Type, Cache-Control)
- [ ] File size < 100KB

### Manual Testing

1. **Validate JSON syntax:**
   ```bash
   cat ai-discovery.json | jq .
   ```

2. **Validate against schema:**
   ```bash
   ajv validate -s v2.0.json -d ai-discovery.json
   ```

3. **Test HTTP endpoint:**
   ```bash
   curl -I https://yourdomain.com/ai-discovery.json
   # Verify: Content-Type: application/json
   # Verify: HTTP 200 OK
   ```

4. **Check file size:**
   ```bash
   wc -c ai-discovery.json
   # Should be < 100,000 bytes
   ```

---

## Support

### Resources

- **Full Specification:** [SPECIFICATION.md](../SPECIFICATION.md)
- **v2.0 Schema:** [schemas/v2.0.json](../schemas/v2.0.json)
- **v2.0 Example:** [examples/v2/ai-discovery.json](../examples/v2/ai-discovery.json)
- **Changelog:** [CHANGELOG.md](../CHANGELOG.md)

### Contact

- **Email:** ai-discovery@pressonify.ai
- **GitHub Issues:** https://github.com/BuddySpuds/AI-Discovery-Protocol/issues
- **GitHub Discussions:** https://github.com/BuddySpuds/AI-Discovery-Protocol/discussions

---

## FAQ

### Q: Do I have to migrate immediately?

**A:** No. v1.0 files will continue to work. However, v2.0 provides enhanced capabilities that AI systems can leverage for better discovery and optimization transparency.

### Q: Is v2.0 backward compatible?

**A:** Yes. All new fields are optional. v1.0 files remain valid, though the version field should be updated to "2.0" for proper schema validation.

### Q: What happens if I don't add the new optional fields?

**A:** Your file will still be valid. However, AI systems won't know about your capabilities (versioning, incremental updates) or have a support contact.

### Q: Can I keep both optimizationStatus and optimization?

**A:** Yes, during the transition period. This ensures backward compatibility with consumers that only understand v1.0. Remove `optimizationStatus` when all consumers upgrade.

### Q: What is the 8-factor scoring model?

**A:** The "adp-v2.0-8factor" scoring model evaluates entities across 8 dimensions:
1. Title optimization
2. Description quality
3. Schema.org markup completeness
4. Image optimization (alt text, file names)
5. Internal linking
6. Content length and structure
7. Keyword relevance
8. Mobile optimization

### Q: How do I calculate baselineScoreRange?

**A:** Run optimization on a representative sample (50-100 entities) without prior optimization. The baseline range is [min_score, max_score] from this sample. This provides a reference point for measuring improvement.

---

**Last Updated:** December 2, 2025
**Version:** 1.0
**Status:** Official Migration Guide
