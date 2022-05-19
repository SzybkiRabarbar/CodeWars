from are_numbers_odd import are_numbers_odd
from random import randrange

def random_numbers():
    result = []
    for _ in range(randrange(10,20)):
        data_type = randrange(0,4)
        if data_type==0:
            temp=[randrange(-1000,1000) for __ in range(randrange(2,10))]
            result.append(temp)
        elif data_type==1:
            temp=tuple([randrange(-1000,1000) for __ in range(randrange(2,10))])
            result.append(temp)
        else:
            result.append(randrange(-1000,1000))
    return result

if __name__ == '__main__':
    content = []
    for _ in range(1):
        numbers = random_numbers()
        print(f"        {[numbers, are_numbers_odd(numbers)]},")