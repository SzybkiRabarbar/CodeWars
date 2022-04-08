'''
https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/python
'''

def first_non_repeating_letter(string:str):
    string_low=string.lower()
    dykta = {letter: string_low.count(letter) for letter in string_low}
    for letter in dykta:
        if dykta.get(letter)==1:
            if letter in string:
                return letter
            else:
                return letter.upper()
    return ''

print(first_non_repeating_letter('sTreSS'))