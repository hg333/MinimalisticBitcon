import json
from messageTypes.addr import addr
from messageTypes.pong import pong
from messageTypes.alert import alert
from messageTypes.version import version
from methods import intFromHex, strFromHex
import struct



class message:
    def __init__(self,recievedMessage):
        cp = recievedMessage
        try:
            self.magic = recievedMessage[:8];recievedMessage=recievedMessage[8:]
            self.command=recievedMessage[:24];recievedMessage=recievedMessage[24:]
            self.command=strFromHex(self.command)
            self.length=recievedMessage[:8];recievedMessage=recievedMessage[8:];self.length=intFromHex(self.length)
            self.checksum = recievedMessage[:8];recievedMessage=recievedMessage[8:];self.checksum=intFromHex(self.checksum)
            self.payload = recievedMessage[:2*self.length];recievedMessage=recievedMessage[2*self.length:]
            self.remS=recievedMessage
            if(self.command.startswith("version")):
                self.payload=version(self.payload)
            elif(self.command.startswith("alert")):self.payload=alert(self.payload)
            elif(self.command.startswith("ping") or self.command.startswith("pong")):self.payload=pong(self.payload)
            # elif(self.command.startswith("addr")):self.payload=addr(self.payload)
        except:
            print(cp)
            self.remS=''
    def rem(self):
        k = self.remS
        self.__delattr__("remS")
        return k
    def __repr__(self) -> str:
        return str(vars(self))
# m = message(" ")
# print(m)