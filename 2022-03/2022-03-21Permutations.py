'''
https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
'''
from itertools import permutations as permutation
def permutations(string):    
    return [''.join(p) for p in set(permutation(string))]

print(permutation('aabb'))
