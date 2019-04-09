import struct
from typing import Tuple


def serialize_var_int(i: int) -> bytes:
    stream = bytes()

    if i < 0:
        raise ValueError("var_int can't be negative")
    elif i < 0xfd:
        stream += bytes([i])
    elif i <= 0xffff:
        stream += bytes([0xfd])
        stream += struct.pack(b'<H', i)
    elif i <= 0xffffffff:
        stream += bytes([0xfe])
        stream += struct.pack(b'<I', i)
    else:
        stream += bytes([0xff])
        stream += struct.pack(b'<Q', i)

    return stream


def deserialize_var_int(stream: bytes) -> Tuple[int, bytes]:
    i = stream[0]
    if i < 0xfd:
        return i, stream[1:]
    elif i == 0xfd:
        return struct.unpack(b'<H', stream[1:3])[0], stream[3:]
    elif i == 0xfe:
        return struct.unpack(b'<I', stream[1:5])[0], stream[5:]
    else:
        return struct.unpack(b'<Q', stream[1:9])[0], stream[9:]