---
title: get_block_number
description: Returns the block number of the most recent block on specified Chain.
---

# get_block_number

Returns the block number of the most recent block on specified
[Chain](/docs/chain).

## Usage

```python
from milapy import Chain

mainnet = Chain(id=1)
block_number = mainnet.get_block_number()
block_number # 18719286
```

## Returns

`int`

The function returns an integer representing the block number.

## Parameters

### cache_ttl (optional)

- **Type**: `int`
- **Default**: [Chain's `cache_ttl`](/docs/chain/#cache_ttl-optional)

The `cache_ttl` parameter is an optional integer that determines the time, in
milliseconds, for which the cached block number will be stored in memory.

Here's how you can use it:

```python
block_number = mainnet.get_block_number(cache_ttl=5_000)
```

By default, the block numbers are cached according to the `cache_ttl` set in the
`Chain`. However, if you set a non-zero value for `cache_ttl`, the block number
will remain in the cache for that specific duration.

Here's what you can do with different `cache_ttl` values:

- Setting `cache_ttl` to a value above zero will keep the block number cached
  for the specified period.
- Setting `cache_ttl` to `0` will disable the cache, ensuring that a fresh block
  number is retrieved every time.

Please note that the underlying caching mechanism uses
[@functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache).

## JSON-RPC Method

[`eth_blockNumber`](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_blocknumber)
