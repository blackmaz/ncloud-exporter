from typing import NamedTuple, Optional


class ResponseData(NamedTuple):
    status: int
    text: str
    json: Optional[dict]
