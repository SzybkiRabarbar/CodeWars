'''
https://www.codewars.com/kata/541c8630095125aba6000c00
Given n, take the sum of the digits of n.
If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
'''

def digital_root(n: int):
    summary = 0
    for i in str(n):
        summary += int(i)
    if summary > 9:
        return digital_root(summary)
    return summary

print(digital_root(1))