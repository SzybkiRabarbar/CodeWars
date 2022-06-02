# https://www.codewars.com/kata/54c27a33fb7da0db0100040e
from math import sqrt

def is_square(n):
    if n<0: return False
    return sqrt(n).is_integer()