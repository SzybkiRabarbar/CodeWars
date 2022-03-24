'''
https://www.codewars.com/kata/54d7660d2daf68c619000d95/python
'''
import math
import functools

def convert_fracts(lst):
    lcm = lambda a, b : abs(a*b) // math.gcd(a, b)
    tmp_list = list(map(lambda x : x[1] ,list(lst)))
    lcm_num = functools.reduce(lcm,tmp_list)
    return list(map(lambda x : [x[0] * lcm_num // x[1], lcm_num] , list(lst)))



'''
import math
def convert_fracts(lst):
    b = []
    if lst == b: return b
    greater = max([l[1] for l in lst if l[1]])
    greater2 = max([l[1] if l[1] != greater else 0 for l in lst if l[1]])
    greater3 = max([l[1] if l[1] != greater and greater2 else 0 for l in lst if l[1]])
    lcm = greater*greater2 // math.gcd(greater2 ,greater)
    if lcm%greater3 != 0: lcm = lcm*greater3 // math.gcd(greater3 ,lcm)
    for l in lst:
        l[0]=int(l[0]*lcm/l[1])
        l[1]=int(l[1]*lcm/l[1])
        b.append(l)
    return b
'''



'''
def convert_fracts(lst):
    b = []
    if lst == b: return b
    greater = max([l[1] for l in lst if l[1]])
    #print(greater)
    while True:
        if greater%lst[0][1] == 0 and greater%lst[1][1] == 0 and greater%lst[2][1] == 0:
            for l in lst:
                l[0]=int(l[0]*greater/l[1])
                l[1]=int(l[1]*greater/l[1])
                b.append(l)
            return b
        greater += 1    
'''




'''
if lst[0][1] > lst[1][1]: greater = lst[0][1]
elif lst[0][1] > lst[2][1]: greater = lst[0][1]
elif lst[1][1] > lst[0][1]: greater = lst[1][1]
elif lst[1][1] > lst[2][1]: greater = lst[1][1]
elif lst[2][1] > lst[0][1]: greater = lst[2][1]
elif lst[2][1] > lst[1][1]: greater = lst[2][1]
'''

''' 
def convert_fracts(lst):
    content = []
    for i in range(100000000000000000):
        if i:
            n = 0
            for lst_from_lst in lst:
                if i%lst_from_lst[1] == 0:
                    n += 1
            if n == len(lst): 
                for l in lst:
                    l[0]=int(l[0]*i/l[1])
                    l[1]=int(l[1]*i/l[1])
                    content.append(l)
                return content
'''   
a = [[1, 2], [1, 3], [1, 4]]
print(convert_fracts(a))

