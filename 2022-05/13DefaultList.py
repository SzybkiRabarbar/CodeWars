class DefaultList():
    def __init__(self, lst:list , dfv) -> None:
        self.lst = lst
        self.dfv = dfv
    
    def extend(self, lst:list):
        self.lst.extend(lst)
    
    def pop(self, indx):
        return self.lst.pop(indx)
    
    def append(self, val):
        self.lst.append(val)
    
    def remove(self, val):
        self.lst.remove(val)
    
    def insert(self, indx, val):
        self.lst.insert(indx, val)
            
    def __getitem__(self, n):
        try: return self.lst[n]
        except IndexError: return self.dfv
