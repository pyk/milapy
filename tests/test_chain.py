import pytest

from milapy import Chain


def test_chain_id():
    mainnet = Chain(id=1)
    assert mainnet.id == 1


def test_chain_default_rpc_url_error():
    with pytest.raises(Exception) as exception:
        Chain(id=9999999)
    assert (
        str(exception.value)
        == "default rpc_url for chain_id=9999999 is not specified"
    )


def test_chain_default_rpc_url():
    angle = Chain(id=9999999, rpc_url="https://rpc.pyk.sh")
    assert angle.id == 9999999
    assert angle.rpc_url == "https://rpc.pyk.sh"


def test_get_block_number():
    mainnet = Chain(id=1)
    assert mainnet.get_block_number() > 18_000_000
    mainnet = Chain(id=1)
    assert mainnet.get_block_number() > 18_000_000
