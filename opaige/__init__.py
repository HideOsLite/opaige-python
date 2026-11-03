"""The Opaige API for Python (2026-11-03). Every method is one API call, named as in the API reference (opaige.com/developers):

    from opaige import Opaige
    opaige = Opaige(os.environ["OPAIGE_KEY"])
    answer = opaige.check_requirements(passport="IN", destination="FR")
    opaige.send_bookings(body={"bookings": [...]})

A sandbox key answers in the same shape and saves and bills nothing. Standard library only.
"""
from .operations import Operations
from .request import VERSION, OpaigeError, Requester
from .webhooks import verify_webhook


class Opaige(Operations):
    def __init__(self, key: str, base_url: str = "https://opaige.com/api/company/v1", timeout: float = 120.0, max_retries: int = 2) -> None:
        super().__init__(Requester(key, base_url=base_url, timeout=timeout, max_retries=max_retries))


__all__ = ["Opaige", "OpaigeError", "verify_webhook", "VERSION"]
