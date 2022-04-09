'''
https://www.codewars.com/kata/55c6126177c9441a570000cc/python
'''
def order_weight(strng:str):
    if not strng: return ''
    weight_lst = strng.split()
    for i, weight in enumerate(weight_lst):
        temp = [int(n) for n in weight]
        weight_lst[i] = [weight, sum(temp)]
    weight_lst.sort(key=lambda x: x[0])
    weight_lst.sort(key=lambda x: x[1])
    return ' '.join([w[0] for w in weight_lst])

