#https://www.codewars.com/kata/559a28007caad2ac4e000083/python
def fib_lst(num):
    a, b, result = 1, 1, [1,1]
    for _ in range(num - 1):
        a, b = b, a + b
        result.append(b)
    return result

def perimeter(n):
    return 4*sum(fib_lst(n))

print(perimeter(5))