import time
from random import randint, getrandbits

import pytest
from faker import Faker

from bitcoin_node_crawler.messages import Address, Version

f = Faker()


@pytest.fixture
def address():
    return {
        "ip": f.ipv4_public(network=False, address_class=None),
        "port": randint(20, 60000),
        "services": randint(0, (2 ** 8) - 1)
    }


@pytest.fixture
def version(address):
    return {
        'version': 70015,
        'services': randint(0, (2 ** 8) - 1),
        'addr_recv': Address(**address),
        'addr_from': Address(**address),
        "timestamp": int(time.time()),
        "nonce": getrandbits(64),
        "start_height": 123,
        "user_agent": "Satoshi:0.16",
    }


def test_address(address):
    a = Address(**address)
    deserialized = Address.deserialize(a.serialize())

    assert a == deserialized
    assert deserialized.ip == address["ip"]
    assert deserialized.port == address["port"]
    assert deserialized.services == address["services"]


def test_version(version):
    a = Version(**version)
    deserialized = Version.deserialize(a.serialize())

    assert a == deserialized
