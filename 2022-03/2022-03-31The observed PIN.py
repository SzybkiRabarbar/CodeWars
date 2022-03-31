'''
https://www.codewars.com/kata/5263c6999e0f40dee200059d/solutions/python
'''
from itertools import product

dykta = {
        '1':['1','2','4'],
        '2':['2','1','3','5'],
        '3':['3','2','6'],
        '4':['4','1','5','7'],
        '5':['5','2','4','6','8'],
        '6':['6','3','5','9'],
        '7':['7','4','8'],
        '8':['8','5','7','9','0'],
        '9':['9','6','8'],
        '0':['0','8']
        }

def get_pins(observed):
    posibilities = [dykta[ob] for ob in observed]
    content = [''.join(l) for l in list(product(*(posibilities[i] for i in range(len(posibilities)))))]
    return content
     

x = '123'
print(get_pins(x))
