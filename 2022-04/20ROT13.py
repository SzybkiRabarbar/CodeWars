'''
https://www.codewars.com/kata/52223df9e8f98c7aa7000062/python
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