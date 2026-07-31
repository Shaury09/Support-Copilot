---
source: api_auth
doc_type: api_doc
last_updated: 2026-03-18
access_level: public
---

# API Authentication

## Overview
The CloudSync API uses OAuth 2.0 with the authorization code grant. All
requests must include a bearer token in the `Authorization` header.

## Obtaining a token
POST to `/oauth/token` with `client_id`, `client_secret`, and
`authorization_code`. The response includes an `access_token` valid for
1 hour and a `refresh_token` valid for 30 days.

## Refreshing a token
POST to `/oauth/token` with `grant_type=refresh_token` and the
`refresh_token`. This returns a new access token without requiring the
user to log in again.

## Error responses
- `401 invalid_token`: token expired or malformed.
- `403 insufficient_scope`: token is valid but lacks the required scope
  for the requested endpoint.
- `429 rate_limited`: see the API Rate Limits documentation for current
  thresholds.
