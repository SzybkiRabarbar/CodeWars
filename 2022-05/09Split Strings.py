#https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/python
def solution(s):
    if len(s)%2==1: s=s+'_'
    s=iter(s)
    return [f"{letter}{next(s)}" for letter in s]