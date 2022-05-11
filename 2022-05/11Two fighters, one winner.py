#https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/python
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1, fighter2, first_attacker):    
    fighters=[fighter1, fighter2] if fighter1.name == first_attacker else [fighter2, fighter1]
    while True:
        for i,atacker in enumerate(fighters):
            i = 0 if i==1 else 1
            fighters[i].health = fighters[i].health-atacker.damage_per_attack
            if fighters[i].health<=0:
                return atacker.name
            
    