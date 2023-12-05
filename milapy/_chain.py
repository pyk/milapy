import time
from functools import lru_cache
from typing import Optional

import httpx


def get_ttl_hash(ms: int = 5_000) -> int:
    return round((time.time() * 1000) / ms)


@lru_cache()
def get_block_number(
    http_client: httpx.Client, ttl_hash: Optional[int] = None
) -> int:
    payload = {
        "method": "eth_blockNumber",
        "params": [],
        "id": 1,
        "jsonrpc": "2.0",
    }
    r = http_client.post("https://rpc.ankr.com/eth", json=payload)
    json = r.json()
    return int(json["result"], 16)


class Chain:
    def __init__(self, id: int):
        self.id = id
        self.http_client = httpx.Client()

    def get_block_number(self, cache_ttl: int = 5_000) -> int:
        return get_block_number(
            http_client=self.http_client, ttl_hash=get_ttl_hash(ms=cache_ttl)
        )
