'''
https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python
'''
def increment_string(strng:str):
    if not strng: return '1'
    check_len=len(strng)
    number_str=str()
    for num in strng[::-1]:
        if num.isnumeric():
            number_str+=num
        else:
            break
    number_str=number_str[::-1].lstrip('0')
    if not number_str: 
        if strng.endswith('0'):return ''.join(strng.rsplit('0',1))+'1'
        return strng+'1'
    number=int(number_str)+1
    strng=''.join(strng.rsplit(number_str,1))
    if len(strng+str(number))!=check_len: return ''.join(strng.rsplit('0',1))+str(number)
    return strng+str(number)

