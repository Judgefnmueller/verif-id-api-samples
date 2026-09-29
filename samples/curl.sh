#!/usr/bin/env bash
# Verify a Verif-ID certificate by SHA-256 content fingerprint
API_KEY="${VFID_API_KEY:?set VFID_API_KEY first}"

curl -s -X POST https://api.verif-id.com/v1/certificates/verify \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content_hash": "a3f1d7e29b4c08..."
  }'
# Expected response fields: verified, status, content_type, is_ai_generated,
# ai_probability, liveness_verified, issued_at, issuer
