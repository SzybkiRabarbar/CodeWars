from are_numbers_odd import are_numbers_odd
import random

def random_numbers():
    result = []
    for _ in range(random.randrange(5,20)):
        data_type = random.randrange(0,3)
        print(data_type)
        if data_type==0:
            result.append(random.randrange(-50,150))
            #TODO: reszte 
    return result

if __name__ == '__main__':
    content = []
    for _ in range(5):
        numbers = random_numbers()
        content.append([numbers, are_numbers_odd(numbers)]) #!# przekazuje liste nie argsy
    print(content)