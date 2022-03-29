'''
https://www.codewars.com/kata/514b92a657cdc65150000006/python
'''

def solution1(number):
    s=0
    for n in range(number):
        if not n: continue
        if n%3==0 or n%5==0:
            s+=n
    return s

def solution2(number):
    return sum([n for n in range(number) if n%3==0 or n%5==0])
print(solution2(10))
  