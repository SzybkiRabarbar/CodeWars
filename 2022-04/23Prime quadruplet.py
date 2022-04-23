'''
https://www.codewars.com/kata/62632ee70fe6db1c6da6555f/python
https://www.codewars.com/kata/62632ee70fe6db1c6da6555f/train/python
'''
from math import sqrt
def next_prime(n):
	prime=0
	n+=1
	for i in range(2,int(n**0.5)+2):
		if n%i==0:
			prime=0
			break
		prime=1
	if prime==1:
		return n	
	return next_prime(n)

def is_prime(n):
    if (n < 2): return False
    sq = int(sqrt(n))
    for i in range(2, sq + 1):
        if (n % i == 0): return False
    return True

def prime_quadruplet(number):
    if number<=5: return '5,7,11,13'
    while True:
        if is_prime(number) and is_prime(number+2) and is_prime(number+6) and is_prime(number+8):
            return f"{number},{number+2},{number+6},{number+8}"
        number = next_prime(number)
        