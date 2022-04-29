'''
https://www.codewars.com/kata/525d9b1a037b7a9da7000905/python
'''
def search_names(logins):
    return [data for data in logins if data[0].endswith('_')]