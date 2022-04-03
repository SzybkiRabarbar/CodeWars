'''
https://www.codewars.com/kata/52774a314c2333f0a7000688/python
'''

def valid_parentheses(string):
    try:
        if not string.count('(')== string.count(')'): return False
        n = 0
        for letter in string[:]:
            if letter=='(': n += 1
            if letter==')': n -= 1
            if n<0: return False
        return True
    except ValueError:
        return True
print(valid_parentheses('( )))((( )'))