'''
https://www.codewars.com/kata/5672682212c8ecf83e000050/python
'''

def gen_dbl(n):
    u = [1]
    for i in u:
        u.append((2*i) +1)
        u.append((3*i) +1)
        if len(u) > n *10: break   
    yield list(sorted(set(u)))[n]

def dbl_linear(n):
    return next(gen_dbl(n))


print(dbl_linear(60000))