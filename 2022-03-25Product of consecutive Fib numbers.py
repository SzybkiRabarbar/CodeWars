'''
https://www.codewars.com/kata/5541f58a944b85ce6d00006a/python
sus
'''

def productFib(prod):
    fibon = [0,1]
    for i, amongus in enumerate(fibon):
        fibon.append(fibon[-1]+fibon[-2])
        if fibon[i] * fibon[i+1] == prod:
            content = [fibon[i], fibon[i+1], True]
            return content
        elif (fibon[i] * fibon[i+1]) > prod:
            content = [fibon[i], fibon[i+1], False]
            return content


print(productFib(4895))
