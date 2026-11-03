"""Checks that a webhook came from Opaige and was not replayed.

Pass the raw request body exactly as received, the Opaige-Signature header and your endpoint's signing secret:
    Opaige-Signature: t=<unix seconds>,v1=<hex HMAC-SHA256 of "<t>.<raw body>">
"""
import hashlib
import hmac
import json
import time
from typing import Any, Dict, Optional, Union


def verify_webhook(raw_body: Union[str, bytes], signature: Optional[str], secret: str, tolerance_seconds: int = 300, now: Optional[float] = None) -> Dict[str, Any]:
    body = raw_body.decode() if isinstance(raw_body, bytes) else raw_body
    parts = dict(p.strip().split("=", 1) for p in (signature or "").split(",") if "=" in p)
    try:
        t = int(parts.get("t", ""))
    except ValueError:
        raise ValueError("Opaige-Signature is missing or malformed.") from None
    v1 = parts.get("v1")
    if not v1:
        raise ValueError("Opaige-Signature is missing or malformed.")
    if abs((now if now is not None else time.time()) - t) > tolerance_seconds:
        raise ValueError("Opaige-Signature is too old: a replay, or a clock far off.")
    want = hmac.new(secret.encode(), f"{t}.{body}".encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(want, v1):
        raise ValueError("Opaige-Signature does not match this body and secret.")
    return json.loads(body)
