#https://www.codewars.com/kata/5739174624fc28e188000465/python
class PokerHand(object):
    def __init__(self, cards:str):
        self.hand = cards.split()
        self.value = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        self.suit = ['S','H','D','C']
        
    def compare_with(self, other):        
        player = self.check([hand for _, hand in sorted(zip([self.value.index(card[0]) for card in self.hand], self.hand))])
        oponent = self.check([hand for _, hand in sorted(zip([self.value.index(card[0]) for card in other.hand], other.hand))])
        print(player,oponent)
        if player[0]<oponent[0]: return 'Win'
        if player[0]>oponent[0]: return 'Loss'
        if player[1]>oponent[1]: return 'Win'
        if player[1]<oponent[1]: return 'Loss'
        return 'Tie'
    
    def check(self, hand):
        v_lst=[x[0] for x in hand]
        if self.straight_flush(hand): return [0, self.straight(hand)]
        if self.four_of_a_kind(v_lst): return [1, self.four_of_a_kind(v_lst)]
        if self.full_house(v_lst): return [2, [self.three_of_a_kind(v_lst)[0], self.pair(v_lst)[0]]]
        if self.flush(hand): return [3, self.flush(hand)]
        if self.straight(hand): return [4, self.straight(hand)]
        if self.three_of_a_kind(v_lst): return [5, self.three_of_a_kind(v_lst)]
        if self.two_pair(v_lst): return [6, self.two_pair(v_lst)]
        if self.pair(v_lst): return [7, self.pair(v_lst)]
        sassy=sorted([self.value.index(x) for x in v_lst],reverse=True)
        return [8,sassy]
    
    def pair(self, v_lst):
        for i in range(4):
            if v_lst.count(v_lst[i]) == 2: 
                result=[self.value.index(v_lst[i])]
                result.extend(sorted([self.value.index(v) for v in v_lst if not v==v_lst[i]],reverse=True))
                return result
        return False
    
    def two_pair(self, v_lst):    
        temp=set()
        for i in range(5):
            if v_lst.count(v_lst[i]) == 2: temp.add(self.value.index(v_lst[i])+1)
        if len(temp)==2:
            result=[max(temp)]
            result.extend(sorted([self.value.index(v) for v in v_lst if not v in temp],reverse=True))
            return result
        return False
        
    def three_of_a_kind(self, v_lst):
        for i in range(3):
            if v_lst.count(v_lst[i]) == 3:
                result=[self.value.index(v_lst[i])]
                result.extend(sorted([self.value.index(v) for v in v_lst if not v==v_lst[i]],reverse=True))
                return result
        return False
    
    def straight(self, hand):
        if ''.join([x[0] for x in hand]) in ''.join(self.value):
            return self.value.index(hand[3][0])
        return False
        
    def flush(self, hand):
        if (all(hand[0][1] == x[1] for x in hand)): return sorted([self.value.index(x[0]) for x in hand], reverse=True)
        return False
    
    def full_house(self, v_lst):
        if self.three_of_a_kind(v_lst): 
            if self.pair(v_lst): return True
        return False
    
    def four_of_a_kind(self, v_lst):
        for i in range(2):
            if v_lst.count(v_lst[i]) == 4: 
                for indx in range(5):
                    if v_lst[i]!=v_lst[indx]:
                        return [self.value.index(v_lst[i]), self.value.index(v_lst[indx])]
    def straight_flush(self, hand):
        if not self.flush(hand): return False
        return self.straight(hand) 
