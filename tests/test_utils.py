from bitcoin_node_crawler.utils import serialize_var_int, deserialize_var_int


def test_de_serialize_var_int():
    assert 2048 == deserialize_var_int(serialize_var_int(2048))[0]
    assert 256 == deserialize_var_int(serialize_var_int(256))[0]
    assert 12 == deserialize_var_int(serialize_var_int(12))[0]
