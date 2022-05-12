#https://www.codewars.com/kata/5552101f47fc5178b1000050/python
def dig_pow(n, p):
    summ = 0
    for num in str(n):
        summ += int(num)**p
        p+=1
    return summ//n if summ/n==summ//n else -1
