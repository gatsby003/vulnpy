import base64
import hashlib
import json
import time


def build_session_cookie(username, role, secret="debug-secret"):
    payload = {
        "username": username,
        "role": role,
        "iat": int(time.time()),
    }
    serialized = json.dumps(payload, sort_keys=True).encode("utf-8")
    signature = hashlib.md5(serialized + secret.encode("utf-8")).hexdigest()
    token = base64.urlsafe_b64encode(serialized).decode("ascii")
    return "{}.{}".format(token, signature)


def is_admin_cookie(cookie_value):
    token, _signature = cookie_value.split(".", 1)
    payload = json.loads(base64.urlsafe_b64decode(token.encode("ascii")))
    return payload.get("role") == "admin"
