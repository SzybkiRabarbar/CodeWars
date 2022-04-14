'''
https://www.codewars.com/kata/58039f8efca342e4f0000023/python
'''
def changer(string:str)->str:
    vovels=[x for x in'aeiouAEIOU']
    result=[]
    for letter in string:
        if not letter.isalpha(): 
            result.append(letter)
        elif letter=='Z' or letter=='z':
            result.append('a')
        elif letter:
            result.append(chr(ord(letter)+1))
    for i,letter in enumerate(result):
        if letter in vovels:
            result[i]=letter.upper()
        elif letter.isalpha():
            result[i]=letter.lower()
    return ''.join(result)
