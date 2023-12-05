# milapy

milapy is an extensible Python 3 interface designed for Ethereum and various
EVM-based chains. It offers a command-line interface, supports multiple chains,
and provides synchronous and asynchronous APIs.

## Getting started

Install milapy using pip:

```sh
pip install milapy
```

Now, let's get started:

```sh
>>> from milapy import Chain
>>> mainnet = Chain(id=1)
>>> mainnet.get_block_number()
18719286
```

## Acknowledgements

milapy were inspired by or directly modified from many sources, primarily:

- [viem](https://viem.sh/)
- [web3.py](https://web3py.readthedocs.io/en/stable/)
- [ethers.js](https://docs.ethers.org/v5/)
