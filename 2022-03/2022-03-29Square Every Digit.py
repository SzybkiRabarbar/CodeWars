'''
https://www.codewars.com/kata/546e2562b03326a88e000020/solutions/python
'''
def square_digits(num):
    return int(''.join([str(int(n)*int(n)) for n in str(num)]))

print(square_digits(9119))
