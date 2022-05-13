#https://www.codewars.com/kata/53f17f5b59c3fcd589000390/python
class SecureList():    
    def __init__(self, msg:list) -> None:
        self.msg = msg[:]
    
    def __repr__(self) -> str:
        r = f"{self.msg}"
        self.msg = []
        return r
    
    def __str__(self) -> str:
        r = f"{self.msg}"
        self.msg = []
        return r
    
    def __len__(self):
        return len(self.msg)
    
    def __getitem__(self, n):
        return self.msg.pop(n)
    