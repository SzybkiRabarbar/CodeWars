#https://www.codewars.com/kata/556deca17c58da83c00002db/python
def tribonacci(signature:list, n:int):
    if n<=3:
        return signature[:n]
    while len(signature)!=n:
        signature.append(sum(signature[-3:]))
    return signature

print(tribonacci([0.5, 0.5, 0.5], 30))