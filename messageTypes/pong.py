import struct

def intFromHex(str):
    bytelen = bytes.fromhex(str)
    bytelen = struct.unpack("<Q",bytelen)
    return bytelen[0]

class pong:
    def __init__(self,str) -> None:
        self.nonce = intFromHex(str)
    def __repr__(self) -> str:
        return str(vars(self))
