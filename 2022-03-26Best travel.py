'''
https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/python
'''

import time
startTime = time.time()

from itertools import permutations
def choose_best_sum(t, k, ls:list):

    if not ls: return None
    if k > len(ls): return None

    prop = ls.copy()
    amogus = int()
    for sus in range(k):
        amogus += prop.pop(prop.index(min(prop)))
    if amogus > t: return None

    perm = permutations(ls, k)
    len_lst = [sum(p) for p in perm if sum(p)<=t]
    for i in range(t,1,-1):
        if i in len_lst:
            return i


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(430, 5, xs))
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))