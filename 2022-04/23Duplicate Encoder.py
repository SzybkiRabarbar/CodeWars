'''
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python
'''
def duplicate_encode(word:str):
    result=str()
    word=word.lower()
    for letter in word:
        if word.count(letter)>1:
            result+=')'
        else:
            result+='('
    return result