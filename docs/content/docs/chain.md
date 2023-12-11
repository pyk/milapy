# Chain

_TODO(pyk): add docs_

## Import

```python
from milapy import Chain
```

## Usage

Initialize new Chain object with your desired chain ID:

_TODO(pyk): add docs_

## Parameters

### id

- **Type**: `int`

The chain id.

```python
mainnet = Chain(id=1)
```

### rpc_url (optional)

- **Type**: `Optional[str]`
- **Default**: `None`

Common chains, such as Ethereum, will have a default RPC URL. Otherwise, you
need to specify the `rpc_url` manually if the default does not exist.

```python
mainnet = Chain(id=1)
mainnet = Chain(id=1, rpc_url="https://eth-mainnet.g.alchemy.com/v2/...")
```

### cache_ttl (optional)

- **Type**: `Optional[int]`
- **Default**: `5_000`

The `cache_ttl` parameter determines the time, in milliseconds, for which the
cached data will be stored in memory.

```python
mainnet = Chain(id=1, cache_ttl=15_000)
```
