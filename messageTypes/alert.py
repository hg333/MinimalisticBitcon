
from methods import strFromHex

def strFromHex(str):
    s = bytes.fromhex(str)
    return bytes.decode(s,"utf-8")

class alert:
    def __init__(self,str) -> None:
        self.alert = bytes.fromhex(str)

    def __repr__(self) -> str:
        return str(vars(self))
