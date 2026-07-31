---
source: api_rate_limits_2025
doc_type: api_doc
last_updated: 2025-06-01
access_level: public
---

# API Rate Limits

## Standard tier
Standard tier API keys are limited to 60 requests per minute and 20,000
requests per day.

## Enterprise tier
Enterprise tier API keys are limited to 300 requests per minute with no
daily cap.

## Exceeding the limit
Requests beyond the limit receive a `429 rate_limited` response with a
`Retry-After` header indicating the number of seconds to wait.
