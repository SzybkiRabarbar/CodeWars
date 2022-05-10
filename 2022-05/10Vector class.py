#https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4/python
class Vector:
    def __init__(self, lst:list) -> None:
        self.lst = lst
        self = tuple(lst)

    def add(self, vec):
        lst1 = self.lst
        lst2 = vec.lst
        if len(lst1)!=len(lst2): raise(Exception('Len of Vectors numst be equal'))     
        return Vector([a+b for a, b in zip(lst1, lst2)])
    
    def subtract(self, vec):
        lst1 = self.lst
        lst2 = vec.lst
        if len(lst1)!=len(lst2): raise(Exception('Len of Vectors numst be equal'))     
        return Vector([a-b for a, b in zip(lst1, lst2)])
    
    def dot(self, vec):
        lst1 = self.lst
        lst2 = vec.lst
        if len(lst1)!=len(lst2): raise(Exception('Len of Vectors numst be equal'))     
        return sum([a*b for a, b in zip(lst1, lst2)])
    
    def norm(self):
        return sum([i**2 for i in self.lst])**0.5
    
    def equals(self, vc):
        return self.lst == vc.lst
    
    def toString(self):
        return str(tuple(self.lst))