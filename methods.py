import struct

def intFromHex(str):
    bytelen = bytes.fromhex(str)
    bytelen = struct.unpack("I",bytelen)
    return bytelen[0]

def strFromHex(str):
    s = bytes.fromhex(str)
    return bytes.decode(s,"utf-8")