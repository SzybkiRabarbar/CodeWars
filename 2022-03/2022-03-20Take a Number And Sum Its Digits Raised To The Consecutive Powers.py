'''
https://www.codewars.com/kata/5626b561280a42ecc50000d1/solutions/python
The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata.
What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers,
that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.
'''


def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    content = []
    for number in range(a, b+1):
        exp = 0
        for i, n in enumerate(str(number)):
            exp += pow(int(n),(i+1))
        if exp == number: content.append(exp)
    return content

'''
def sum_dig_pow(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]
'''

