# https://www.codewars.com/kata/54ba84be607a92aa900000f1/python
def is_isogram(string:str)->bool:
    return len(string) == len(set(string.lower()))