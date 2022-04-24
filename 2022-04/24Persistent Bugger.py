'''
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/python
'''
def persistence(n):
    result=0
    while len(str(n))>1:
        result+=1
        temp=1
        for number in str(n):
            temp*=int(number)
        n=temp
    return result
