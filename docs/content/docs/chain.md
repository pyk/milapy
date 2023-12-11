# Chain

`Chain` is a python class. Chain object have access to JSON-RPC API methods such
as retrieving block numbers, transactions, reading from smart contracts, etc

## Import

::: code-group

```python [sync.py]
from milapy import Chain
```

```python [async.py]
from milapy.aio import Chain
```

:::

## Usage

Initialize new Chain object with your desired chain ID:

::: code-group

```python [sync.py]
from milapy import Chain
```

```python [async.py]
from milapy.aio import Chain
```

:::

Then you can query the chain data:

::: code-group

```python [sync.py]
as
```

```python [async.py]
sa
```

:::

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
