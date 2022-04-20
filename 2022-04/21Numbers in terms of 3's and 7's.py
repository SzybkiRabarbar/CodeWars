'''
https://www.codewars.com/kata/62524390983b35002c8ff1e5/python
'''
def mul37(num:int)->str:
    number_of_7=int(num/7)
    while number_of_7>=0:
        sum_of_7=number_of_7 * 7
        if (num - sum_of_7)%3==0: return f'3 * {(num - sum_of_7)//3} + 7 * {number_of_7}'
        number_of_7-=1
