---
source: error_code_reference
doc_type: reference
last_updated: 2026-01-05
access_level: public
---

# Error Code Reference

| Code | Meaning | Typical fix |
|---|---|---|
| SYNC-101 | Edit conflict between devices | Merge manually, keep needed version |
| SYNC-204 | Storage quota exceeded | Upgrade plan or delete files |
| SYNC-317 | Device limit reached | Remove a device or upgrade plan |
| AUTH-401 | Invalid or expired token | Refresh the OAuth token |
| AUTH-403 | Insufficient OAuth scope | Re-authorize with required scope |
| RATE-429 | Rate limit exceeded | Wait for the `Retry-After` window |
