'''
https://www.codewars.com/kata/520b9d2ad5c005041100000f/python
'''

from curses.ascii import isalpha

def pig_it1(text:str):
    content = []
    txt_lst = text.split()
    for txt in txt_lst:
        if not isalpha(txt[0]): 
            content.append(txt)
            continue
        first_letter = txt[0]
        txt = txt.replace(first_letter,'',1)
        txt += first_letter+'ay'
        content.append(txt)
    return ' '.join(content)

def pig_it(text:str):
    txt_lst = text.split()
    return ' '.join([txt[1:]+txt[0]+'ay' if isalpha(txt[0]) else txt for txt in txt_lst])

print(pig_it('Pig latin is cool !'))