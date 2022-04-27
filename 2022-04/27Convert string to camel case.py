'''
https://www.codewars.com/kata/517abf86da9663f1d2000003/python
'''
def to_camel_case(text:str)->str:
    if not text: return ''
    first=text[:1]
    for letter in text:
        if letter.isalpha() or letter==' ': continue
        text=text.replace(letter,' ')
    text=text.split()
    text=[t.capitalize() for t in text]
    text[0]=f"{first}{text[0][1:]}"
    return ''.join(text)