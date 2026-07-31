---
source: api_rate_limits_2026
doc_type: api_doc
last_updated: 2026-06-15
access_level: public
---

# API Rate Limits (Updated)

## Standard tier
As of the June 2026 update, Standard tier API keys are limited to 120
requests per minute and 50,000 requests per day.

## Enterprise tier
Enterprise tier API keys are limited to 600 requests per minute with no
daily cap.

## Exceeding the limit
Requests beyond the limit receive a `429 rate_limited` response with a
`Retry-After` header indicating the number of seconds to wait. This
behavior is unchanged from previous versions.
