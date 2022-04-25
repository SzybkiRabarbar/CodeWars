'''
https://www.codewars.com/kata/554b4ac871d6813a03000035/python
'''
def high_and_low(numbers):
    numbers=[int(n) for n in numbers.split()]
    return f'{max(numbers)} {min(numbers)}'