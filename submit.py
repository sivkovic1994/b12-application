import json
import hmac
import hashlib
import urllib.request
from datetime import datetime, timezone

URL = "https://b12.io/apply/submission"
SECRET = b"hello-there-from-b12"

def iso_timestamp():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")

payload = {
    "action_run_link": "https://github.com/YOUR_USERNAME/YOUR_REPO/actions/runs/YOUR_RUN_ID",
    "email": "sladjanivkovic2@gmail.com",
    "name": "Sladjan Ivkovic",
    "repository_link": "https://github.com/sivkovic1994/b12-application",
    "resume_link": "https://drive.google.com/uc?export=download&id=1ZO1apOm8ZmBn7WVrWMxD4jNk4HuND9D_",
    "timestamp": iso_timestamp()
}

body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")

signature = hmac.new(SECRET, body, hashlib.sha256).hexdigest()

req = urllib.request.Request(
    URL,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-Signature-256": f"sha256={signature}"
    },
    method="POST"
)

with urllib.request.urlopen(req) as response:
    print(response.read().decode())