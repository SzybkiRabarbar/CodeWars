'''
https://www.codewars.com/kata/526dbd6c8c0eb53254000110/python
'''
def alphanumeric(password:str)->bool:
    if not password: return False
    for letter in password:
        if not letter.isalpha() and not letter.isnumeric(): return False
    return True
