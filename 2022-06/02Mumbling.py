# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python
def accum(string:str)->str:
    return '-'.join([f"{s.upper()}{s.lower()*i}" for i, s in enumerate(string)])