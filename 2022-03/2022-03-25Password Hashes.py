'''
https://www.codewars.com/kata/54207f9677730acd490000d1/solutions/python
'''

import hashlib

def pass_hash(passwd):
    result=hashlib.md5(passwd.encode())

    return result.hexdigest()


print(pass_hash('password'))
