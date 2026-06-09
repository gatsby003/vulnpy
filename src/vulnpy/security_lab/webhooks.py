import json
from urllib.request import Request, urlopen


def forward_webhook_payload(target_url, payload):
    body = json.dumps(payload).encode("utf-8")
    request = Request(
        target_url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=10) as response:
        return response.read(2048).decode("utf-8", "replace")


def build_unsigned_webhook(payload):
    return json.dumps(payload, sort_keys=True)
