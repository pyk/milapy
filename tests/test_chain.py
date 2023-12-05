from milapy import Chain


def test_chain_id():
    mainnet = Chain(id=1)
    assert mainnet.id == 1


def test_get_block_number():
    mainnet = Chain(id=1)
    assert mainnet.get_block_number() > 18_000_000
