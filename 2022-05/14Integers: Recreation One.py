#https://www.codewars.com/kata/55aa075506463dac6600010d/python
def divisors(n):
    result = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return list(result)

def list_squared(m, n):
    result=[]
    for number in range(m,n):
        #print('===',number,'===')
        div_sum = sum([x**2 for x in divisors(number)])
        div_sqrt = div_sum**.5
        if div_sqrt == int(div_sqrt):
            result.append([number, div_sum])
    return result