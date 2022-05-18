def odd_or_not(num:int)->int:
    return num%2

def is_number_odd(number:int)->int:
    return bool(odd_or_not(number))

def are_numbers_odd(numbers:list)->list:
    return [bool(number) for number in map(odd_or_not, numbers)]

def check_input(*numbers):
    content=[]
    for number in numbers:
        if type(number)==int:
            content.append(is_number_odd(number))
        elif type(number)==list and all([True if type(n)==int else False for n in number]):
            content.append(are_numbers_odd(number))
        else:
            raise Exception('Bad input! Input must be integer or list of integers')
    return content

if __name__=='__main__':
    print(check_input([5,2,2,1,3,4,5],2,3,'a'))
    

