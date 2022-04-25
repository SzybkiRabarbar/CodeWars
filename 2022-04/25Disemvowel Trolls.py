'''
https://www.codewars.com/kata/52fba66badcd10859f00097e/solutions/python
'''
def disemvowel(string_):
    return ''.join([s for s in string_ if not s in 'euioaEUIOA'])