'''
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/python
'''

def zero(func=False): 
    if func:
        if func[0]==1: return 0+func[1]
        if func[0]==2: return 0-func[1]
        if func[0]==3: return 0*func[1]
        if func[0]==4: return 0//func[1]
    else:
        return 0
def one(func=False):
    if func:
        if func[0]==1: return 1+func[1]
        if func[0]==2: return 1-func[1]
        if func[0]==3: return 1*func[1]
        if func[0]==4: return 1//func[1]
    else:
        return 1
def two(func=False):
    if func:
        if func[0]==1: return 2+func[1]
        if func[0]==2: return 2-func[1]
        if func[0]==3: return 2*func[1]
        if func[0]==4: return 2//func[1]
    else:
        return 2
def three(func=False):
    if func:
        if func[0]==1: return 3+func[1]
        if func[0]==2: return 3-func[1]
        if func[0]==3: return 3*func[1]
        if func[0]==4: return 3//func[1]
    else:
        return 3
def four(func=False):
    if func:
        if func[0]==1: return 4+func[1]
        if func[0]==2: return 4-func[1]
        if func[0]==3: return 4*func[1]
        if func[0]==4: return 4//func[1]
    else:
        return 4
def five(func=False):
    if func:
        if func[0]==1: return 5+func[1]
        if func[0]==2: return 5-func[1]
        if func[0]==3: return 5*func[1]
        if func[0]==4: return 5//func[1]
    else:
        return 5
def six(func=False):
    if func:
        if func[0]==1: return 6+func[1]
        if func[0]==2: return 6-func[1]
        if func[0]==3: return 6*func[1]
        if func[0]==4: return 6//func[1]
    else:
        return 6
def seven(func=False):
    if func:
        if func[0]==1: return 7+func[1]
        if func[0]==2: return 7-func[1]
        if func[0]==3: return 7*func[1]
        if func[0]==4: return 7//func[1]
    else:
        return 7
def eight(func=False):
    if func:
        if func[0]==1: return 8+func[1]
        if func[0]==2: return 8-func[1]
        if func[0]==3: return 8*func[1]
        if func[0]==4: return 8//func[1]
    else:
        return 8
def nine(func=False):
    if func:
        if func[0]==1: return 9+func[1]
        if func[0]==2: return 9-func[1]
        if func[0]==3: return 9*func[1]
        if func[0]==4: return 9//func[1]
    else:
        return 9

def plus(num): return [1,num]
def minus(num): return [2,num]
def times(num): return [3,num]
def divided_by(num): return [4,num]