// Verify a Verif-ID certificate by SHA-256 content fingerprint
const API_KEY = process.env.VFID_API_KEY;

async function verifyCertificate(contentHash) {
  const res = await fetch("https://api.verif-id.com/v1/certificates/verify", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ content_hash: contentHash }),
  });
  if (!res.ok) throw new Error(`Verif-ID API error: ${res.status}`);
  return res.json();
  // { verified, status, content_type, is_ai_generated, ai_probability,
  //   liveness_verified, issued_at, issuer }
}

verifyCertificate("a3f1d7e29b4c08...").then(console.log);
