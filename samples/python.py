"""Verify a Verif-ID certificate by SHA-256 content fingerprint."""
import os, json, urllib.request

API_KEY = os.environ["VFID_API_KEY"]

def verify_certificate(content_hash: str) -> dict:
    req = urllib.request.Request(
        "https://api.verif-id.com/v1/certificates/verify",
        data=json.dumps({"content_hash": content_hash}).encode(),
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)

if __name__ == "__main__":
    result = verify_certificate("a3f1d7e29b4c08...")
    print(json.dumps(result, indent=2))
    # { "verified": true, "status": "verified", "content_type": "image",
    #   "is_ai_generated": false, "ai_probability": 0.04,
    #   "liveness_verified": true, "issued_at": "...", "issuer": "..." }
