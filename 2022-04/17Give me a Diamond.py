'''
https://www.codewars.com/kata/5503013e34137eeeaa001648/python
'''
def diamond(n):
    if n%2==0 or n<0: return None
    center=n//2
    n=0
    result=str()
    temp=''.join([' 'for i in range(center)]) +'*\n'
    while True:
        result+=temp
        if not ' ' in temp: break
        temp='**'.join(temp.rsplit(' ',1))
    while n<center:
        n+=1
        temp=temp.replace('**',' ',1)
        result+=temp
    return result
