'''https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/python
'''
def max_sequence(arr):
    if not arr: return 0
    content=[]
    for indx in range(len(arr)):
        for i in range(indx,len(arr)):
            content.append([indx,i])
    result = sorted([sum(arr[x[0]:x[1]+1]) for x in content],reverse=True)[0]
    if result<0: return 0
    return result