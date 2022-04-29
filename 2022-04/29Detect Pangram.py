'''
https://www.codewars.com/kata/545cedaa9943f7fe7b000048/python
'''
def is_pangram(s):
    s=s.lower()
    alp='abcdefghijklmnopqrstuvwxyz'
    for letter in alp:
        if not letter in s: return False
    return True