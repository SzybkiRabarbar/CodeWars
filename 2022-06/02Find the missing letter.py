# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/python
from string import ascii_lowercase, ascii_uppercase

def find_missing_letter(chars:list):   
    if chars[0].islower():
        indx = ascii_lowercase.index(chars[0])
        for char in chars:
            if char == ascii_lowercase[indx]:
                indx+=1
                continue
            return ascii_lowercase[indx]
    else:
        indx = ascii_uppercase.index(chars[0])
        for char in chars:
            if char == ascii_uppercase[indx]:
                indx+=1
                continue
            return ascii_uppercase[indx]