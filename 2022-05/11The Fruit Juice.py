#https://www.codewars.com/kata/5264603df227072e6500006d/python
class Jar():
    def __init__(self):
        self.dct=dict()
        pass
    
    def add (self, amount, kind):
        if kind in self.dct:
            self.dct[kind] = self.dct[kind]+amount
        else:
            self.dct[kind] = amount
    
    def pour_out (self, amount):
        amount = amount/len(self.dct)
        for key, value in self.dct.items():
            self.dct[key] = value-amount
    
    def get_total_amount(self):
        return sum([value for _, value in self.dct.items()])
    
    def get_concentration(self, kind):
        if kind in self.dct:
            return self.dct.get(kind)/self.get_total_amount()
        return 0
