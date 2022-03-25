def productFib(prod):
    fibon = [0,1,1,2]
    for i in range(20):
        fibon.append(fibon[-1]+fibon[-2])
    return fibon
