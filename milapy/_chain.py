import time
from functools import lru_cache
from typing import Optional

import httpx

# from pydantic import BaseModel


def get_ttl_hash(ms: int = 5_000) -> int:
    return round((time.time() * 1000) / ms)


@lru_cache()
def get_block_number(
    http_client: httpx.Client, rpc_url: str, ttl_hash: Optional[int] = None
) -> int:
    payload = {
        "method": "eth_blockNumber",
        "params": [],
        "id": 1,
        "jsonrpc": "2.0",
    }
    r = http_client.post(rpc_url, json=payload)
    json = r.json()
    return int(json["result"], 16)


class Chain:
    def __init__(self, id: int, rpc_url: Optional[str] = None):
        self.id = id
        self.http_client = httpx.Client()
        self.rpc_url = rpc_url or self.get_default_rpc_url(id)

    def get_default_rpc_url(self, id: int) -> str:
        if id == 1:
            return "https://cloudflare-eth.com"
        else:
            raise Exception(
                f"default rpc_url for chain_id={id} is not specified"
            )

    def get_block_number(self, cache_ttl: int = 5_000) -> int:
        return get_block_number(
            http_client=self.http_client,
            rpc_url=self.rpc_url,
            ttl_hash=get_ttl_hash(ms=cache_ttl),
        )
