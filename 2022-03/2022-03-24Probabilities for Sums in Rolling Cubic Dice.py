'''
https://www.codewars.com/kata/56f78a42f749ba513b00037f/python
'''

import itertools
def rolldice_sum_prob(sum_, dice_amount):
        
    sums  = [sum(i) for i in itertools.product([1,2,3,4,5,6], repeat=dice_amount)]
    cou = sums.count(sum_)
    prob  = cou/(6**dice_amount)
    
    return prob

   

print(rolldice_sum_prob(10, 3))
