'''
https://www.codewars.com/kata/52ad1db4b2651f744d000394/solutions/python
'''
def reindeer(presents):
    if presents>180: return 1/0
    result=2
    if presents%30:result+=1
    result+=presents//30
    return result
    