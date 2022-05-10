#https://www.codewars.com/kata/590148d79097384be600001e/python
def sort_by_guide(arr:list, guide:list)->list:
    result = [y for x , y in sorted(zip(guide, arr)) if x != -1]
    for i,x in enumerate(guide):
        if x != -1: continue
        result.insert(i, arr[i])
    return result