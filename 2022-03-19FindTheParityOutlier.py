'''
https://www.codewars.com/kata/5526fc09a1bbd946250002dc
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
 The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
  Write a method that takes the array as an argument and returns this "outlier" N.
'''

def find_outlier(integers):
    even = []
    odd = []
    [even.append(inte) if (inte%2) == 0 else odd.append(inte) for inte in integers]
    if len(even) > len(odd):
        return odd[0]
    else:
        return even[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
    