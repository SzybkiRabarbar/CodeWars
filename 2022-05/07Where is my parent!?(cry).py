from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
def find_children(dancing_brigade:str)->str:    
    ord=''.join([x+y for x,y in zip(uc,lc)])
    return ''.join(sorted([x for x in dancing_brigade], key=lambda o: ord.index(o)))
