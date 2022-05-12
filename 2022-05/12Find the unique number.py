#https://www.codewars.com/kata/585d7d5adb20cf33cb000235/solutions/python
def find_uniq(arr:list):
    return [n for n in set(arr) if arr.count(n)==1][0]