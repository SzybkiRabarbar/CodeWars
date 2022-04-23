'''
https://www.codewars.com/kata/54e6533c92449cc251001667/python
'''
def unique_in_order(iterable:list):
    result = []
    for el in iterable:
        if result and result[-1]==el: continue
        result.append(el)
    return result 