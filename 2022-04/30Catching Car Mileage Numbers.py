'''
https://www.codewars.com/kata/52c4dd683bfd3b434c000292/python
'''

def check_intrest(number:int, awesome_phrases:list):
    number_str=str(number)

    if number<100: return False # A number is only interesting if it is greater than 99
    if number in awesome_phrases: return True # The digits match one of the values in the awesome_phrases array
    if len(number_str.replace('0',''))==1: return True # Any digit followed by all zeros
    if len(set(number_str))==1: return True # Every digit is the same number

    for i, num in enumerate(number_str): # The digits are sequential, incementing
        if i+1==len(number_str): return True
        if not (int(number_str[i+1])-int(num)==1): 
            if (num=='9' and number_str[i+1]=='0'): continue
            break

    for i, num in enumerate(number_str): # The digits are sequential, decrementing
        if i+1==len(number_str): return True
        if not (int(number_str[i+1])-int(num)==(-1)): 
            if (num=='1' and number_str[i+1]=='0'): continue
            break
    
    # The digits are a palindrome
    f_half=number_str[:(len(number_str)//2)]
    s_half=number_str[-(len(number_str)//2):]
    print(f_half, s_half)
    if f_half == s_half[::-1]: return True
    return False

def is_interesting(number:int, awesome_phrases:list):
    if check_intrest(number, awesome_phrases): return 2
    if check_intrest(number+1, awesome_phrases): return 1
    if check_intrest(number+2, awesome_phrases): return 1
    return 0

#rozwiazanie z codewars
'''
def is_incrementing(number): return str(number) in '1234567890'
def is_decrementing(number): return str(number) in '9876543210'
def is_palindrome(number):   return str(number) == str(number)[::-1]
def is_round(number):        return set(str(number)[1:]) == set('0')

def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)
       
    for num, color in zip(range(number, number+3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0
'''
