from methods import intFromHex, strFromHex


class version:
    def __init__(self,str) -> None:
        self.version=intFromHex(str[0:8])
    def __repr__(self) -> str:
        return str(vars(self))
