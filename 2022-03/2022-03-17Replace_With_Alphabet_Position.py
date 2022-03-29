'''
https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
'''
def alphabet_position(text):
    alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']   
    result = str()
    for l in text:
        try:
            i = alphabet.index(l.lower())
            result = result +" "+ str(i+1)
        except ValueError:
            continue
    return result.strip()
print(alphabet_position("The sunset sets at twelve o' clock."))

