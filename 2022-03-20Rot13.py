'''
https://www.codewars.com/kata/530e15517bc88ac656000716/python
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''
def rot13(message):
    content = str()
    for m in message:
        if m.isalpha():
            if m.islower():
                nm = ord(m)
                if nm>109:
                    content += str(chr(nm-13))
                else:
                    content += str(chr(nm+13))
            else:
                nm = ord(m)
                if nm>77:    
                    content += str(chr(nm-13))
                else:
                    content += str(chr(nm+13))
        else:
            content += m
    return content

print(rot13("6chU@steczki9"))
