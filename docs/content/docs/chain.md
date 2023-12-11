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

### cache_ttl (optional)

- **Type**: `int`
- **Default**: `5_000`

The `cache_ttl` parameter determines the time, in milliseconds, for which the
cached data will be stored in memory.

```python
mainnet = Chain(id=1, cache_ttl=15_000)
```
