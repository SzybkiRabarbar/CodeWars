'''
https://www.codewars.com/kata/54da5a58ea159efa38000836/python
'''

def find_it(seq):
    for s in seq:
        if not (seq.count(s))%2==0: return s

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))