def odd_or_not(num:int)->int:
    return bool(num%2)

def are_iter_odd(numbers:list)->list:
    return [number for number in map(odd_or_not, numbers)]

def are_numbers_odd(*numbers):
    content=[]
    for number in numbers:
        if isinstance(number, int):
            content.append(odd_or_not(number))
        elif number and isinstance(number, (list, set, tuple)) and all([True if isinstance(n, int) else False for n in number]):
            content.append(are_iter_odd(number))
        else:
            return f"Wrong input: '{number}', index: {numbers.index(number)}"
    return content

if __name__=='__main__':
    print(are_numbers_odd(1,[2,3],4,[5,'v']))
    
    # test.assert_equals()
    

