# Changelog

## 2026-09-29

- Initial public sample set: `curl`, `python`, and `javascript` examples for
  certificate verification (`POST /v1/certificates/verify`).

## Current API surface (as documented at https://myverif-id.base44.app/api-docs)

- `POST /v1/certificates/verify` — verify by SHA-256 content fingerprint
- `GET /v1/certificates/:id` — certificate metadata by ID
- `POST /v1/analyze` — forensic analysis without a liveness check
