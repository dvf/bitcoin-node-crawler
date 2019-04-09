import struct as s
import time
from dataclasses import dataclass
from hashlib import sha256

from bitcoin_node_crawler.utils import deserialize_var_int, serialize_var_int


@dataclass
class Message:
    def compile(self):
        message_name = getattr(self, "MESSAGE_NAME")
        payload = getattr(self, "serialize")()

        # magic value for Main net
        magic = bytes.fromhex("F9BEB4D9")
        command = message_name + (12 - len(message_name)) * "\00"
        length = s.pack("I", len(payload))

        # Bitcoin checksums only use the first 4 bytes
        checksum = sha256(sha256(payload).digest()).digest()[:4]

        return magic + command.encode() + length + checksum + payload


@dataclass
class Address(Message):
    MESSAGE_NAME = "net_addr"

    ip: str
    port: int
    services: int = 0

    def serialize(self):
        return s.pack("<Q", self.services) + s.pack("<16s", self.ip.encode()) + s.pack("<H", self.port)

    @classmethod
    def deserialize(cls, payload: bytes):
        services = s.unpack("<Q", payload[0:8])[0]
        ip = s.unpack("<16s", payload[8:24])[0].split(b'\0', 1)[0].decode("utf8")
        port = s.unpack("<H", payload[24:26])[0]

        return cls(services=services, ip=ip, port=port)


@dataclass
class Version(Message):
    MESSAGE_NAME = "version"

    version: int
    services: int
    timestamp: int
    nonce: int
    start_height: int
    user_agent: str
    addr_recv: Address
    addr_from: Address

    def serialize(self):
        version = s.pack("<i", self.version)
        services = s.pack("<Q", self.services)
        timestamp = s.pack("<q", int(time.time()))
        addr_recv = self.addr_recv.serialize()
        addr_from = self.addr_from.serialize()
        nonce = s.pack("<Q", self.nonce)
        user_agent = serialize_var_int(len(self.user_agent)) + self.user_agent.encode("ascii")
        start_height = s.pack("<i", self.start_height)
        return version + services + timestamp + addr_recv + addr_from + nonce + user_agent + start_height

    @classmethod
    def deserialize(cls, payload: bytes):
        version = s.unpack("<i", payload[:4])[0]
        services = s.unpack("<Q", payload[4:12])[0]
        timestamp = s.unpack("<q", payload[12:20])[0]
        addr_recv = Address.deserialize(payload[20:46])
        addr_from = Address.deserialize(payload[46:72])
        nonce = s.unpack("<Q", payload[72:80])[0]

        user_agent_length, payload = deserialize_var_int(payload[80:])
        user_agent = payload[0:user_agent_length].decode("utf8")
        start_height = s.unpack("<i", payload[user_agent_length: user_agent_length + 4])[0]

        return cls(version=version, services=services, timestamp=timestamp, addr_recv=addr_recv, addr_from=addr_from,
                   nonce=nonce, user_agent=user_agent, start_height=start_height)

#
# v = Version(version=70015, services=0, addr_recv=Address(ip="127.0.0.1", port=8889), addr_from=Address(ip="127.0.0.1",
#                                                                                                        port=8889),
#             nonce=random.getrandbits(64), start_height=123, user_agent="synapse:0.1")
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(("173.249.0.235", 8333))
# sock.send(v.compile())
# r = sock.recv(1024)  # version
# r1 = sock.recv(1024)  # verack
# print(r, r1)
