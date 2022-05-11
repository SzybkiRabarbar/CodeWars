#https://www.codewars.com/kata/5264603df227072e6500006d/python
class Jar():
    def __init__(self):
        self.dct = dict()

    def add (self, amount, kind):
        if kind in self.dct:
            self.dct[kind] += amount
        else:
            self.dct[kind] = amount
    
    def pour_out (self, amount):
        proportion = amount / self.get_total_amount()
        for key, value in self.dct.items():
            self.dct[key] = value * (1 - proportion)
    
    def get_total_amount(self):
        return sum(self.dct.values()) 
    
    def get_concentration(self, kind):
        if kind in self.dct:
            return self.dct[kind] / self.get_total_amount()
        return 0
