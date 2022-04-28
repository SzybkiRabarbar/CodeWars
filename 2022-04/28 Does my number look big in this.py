'''
https://www.codewars.com/kata/5287e858c6b5a9678200083c/python
'''
def narcissistic( value ):
        temp=0
        for number in str(value):
            temp+=int(number)**len(str(value))
        if temp==value: return True
        return False
