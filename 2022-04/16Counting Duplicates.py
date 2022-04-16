'''
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/python
'''
def duplicate_count(text:str):
    text=text.lower()
    content=set()
    for letter in text:
        if text.count(letter)>1: content.add(letter)
    return len(content)

