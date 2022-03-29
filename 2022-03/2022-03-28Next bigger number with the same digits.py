'''
https://www.codewars.com/kata/55983863da40caa2c900004e/python
'''
from itertools import permutations
'''
def next_bigger(n):
    perm = permutations(str(n))
    number_lst = (int(''.join([n for n in n_lst])) for n_lst in perm if int(''.join([n for n in n_lst]))>n)
    number_lst = sorted(list(set(number_lst)))
    indx = number_lst.index(n)
    if number_lst[indx] == number_lst[-1]: return -1
    content = number_lst[indx+1]
    return content
'''
def next_bigger(n):
    nn = str(n)[:]
    if len(str(n)) > 6:
        rest_n = str(n)[:-5]
        n = str(n)[-5:]
    perm = sorted(list(set(permutations(str(n)))))
    number = tuple(nb for nb in str(n))
    indx = perm.index(number)
    if perm[indx] == perm[-1]: return -1
    new = ''.join(perm[indx+1])
    if len(str(nn)) > 6:
        return int(rest_n + new)
    return int(new)

print(next_bigger(59884848459853))
