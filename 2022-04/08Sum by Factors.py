'''
https://www.codewars.com/kata/54d496788776e49e6b00052f/python
'''
def sum_for_list(lst:list):
    content=[]
    result = set()
    prime_numbers=set()
    for n in lst:
        if n<0: n=-n
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                result.add(i)
                result.add(n//i)
    for n in result:
        temp=set()
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                temp.add(i)
                temp.add(n//i)
        if len(temp)==2: prime_numbers.add(n)  
    for factor in prime_numbers:
        numbers_divided_by_factor = [number for number in lst if number%factor==0]
        content.append([factor, sum(numbers_divided_by_factor)]) 
    return sorted(content)


        

