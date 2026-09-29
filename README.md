# Verif-ID Forensics API Samples

Code samples for the **Verif-ID Forensics API** — integrate authenticity verification directly into your platform.

Live product: https://myverif-id.base44.app

## API overview

- **Format:** JSON / REST
- **Base URL:** `https://api.verif-id.com/v1`
- **Auth:** API key, passed as `Authorization: Bearer vfid_live_xxxxxxxx` or in the request body
- **Keys:** available in your account dashboard; contact support for production access

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/v1/certificates/verify` | Verify a certificate by its SHA-256 content fingerprint |
| GET  | `/v1/certificates/:id` | Retrieve full certificate metadata by certificate ID |
| POST | `/v1/analyze` | Submit content for AI forensic analysis without a liveness check |

## Samples

- [`curl`](./samples/curl.sh)
- [`python`](./samples/python.py)
- [`javascript`](./samples/javascript.js)

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).
