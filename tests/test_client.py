import milapy


def test_get_block_number():
    client = milapy.Client()
    assert client.get_block_number() == 0
