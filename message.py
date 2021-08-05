import json
import struct

def intFromHex(str):
    bytelen = bytes.fromhex(str)
    bytelen = struct.unpack("I",bytelen)
    return bytelen[0]

class message:
    def __init__(self,recievedMessage):
        #recievedMessage="f9beb4d9616c65727400000000000000a80000001bf9aaea60010000000000000000000000ffffff7f00000000ffffff7ffeffff7f01ffffff7f00000000ffffff7f00ffffff7f002f555247454e543a20416c657274206b657920636f6d70726f6d697365642c2075706772616465207265717569726564004630440220653febd6410f470f6bae11cad19c48413becb1ac2c17f908fd0fd53bdc3abd5202206d0e9c96fe88d4a0f01ed9dedae2b6f9e00da94cad0fecaae66ecf689bf71b50"
        self.magic = recievedMessage[:8];recievedMessage=recievedMessage[8:]
        self.command=recievedMessage[:24];recievedMessage=recievedMessage[24:]
        self.command=bytes.fromhex(self.command);self.command=bytes.decode(self.command,"utf-8")
        self.length=recievedMessage[:8];recievedMessage=recievedMessage[8:];self.length=intFromHex(self.length)
        self.checksum = recievedMessage[:8];recievedMessage=recievedMessage[8:];self.checksum=intFromHex(self.checksum)
        self.payload = recievedMessage[:2*self.length];recievedMessage=recievedMessage[2*self.length:]
        self.remS=recievedMessage
    def rem(self):
        k = self.remS
        self.__delattr__("remS")
        return k
    def __repr__(self) -> str:
        return str(vars(self))
        return ""

# m = message(" ")
# print(m)