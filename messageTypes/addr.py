
import struct

def intFromHex(str):
    bytelen = bytes.fromhex(str)
    bytelen = struct.unpack("I",bytelen)
    return bytelen[0]

def strFromHex(str):
    str=str.strip()
    s = bytes.fromhex(str).strip()
    return bytes.decode(s,"utf-8")

class addr:
    def __init__(self,str) -> None:
        self.org=str
        return
        if(len(str)>30): return
        self.nums = bytes.fromhex(str[0:2])
        str=str[2:]
        self.nums=struct.unpack('b',self.nums)
        print(self.nums)
        self.addlist=[]
        while len(str)>0:
            timestamp = str[:8];str=str[8:]
            # timestamp=intFromHex(timestamp)
            # time=str[:8];str=str[8:]
            services=str[:16];str=str[16:]
            # services=bytes.fromhex(services)
            # services=struct.unpack("Q",services)
            IP=str[:32];str=str[32:]
            # print(IP)
            port=str[:4];str=str[4:]
            port=bytes.fromhex(port)#;port=struct.unpack('>H',port)
            self.addlist.append((timestamp,services,IP,port))

    def __repr__(self) -> str:
        return str(vars(self))

