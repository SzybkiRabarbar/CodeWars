#https://www.codewars.com/kata/5dad6e5264e25a001918a1fc/train/python
def decode(r:str):
    NUMBERS_FOR_LETTERS = {i-97: chr(i)for i in range(97,123)}
    number=str()
    for num in r:
        if not num.isnumeric(): break
        number+=num
    random_number=int(number)
    decode_check=[(number*random_number)%26 for number in NUMBERS_FOR_LETTERS]
    if any([decode_check.count(x)-1 for x in decode_check]): return 'Impossible to decode'   
    decode_key={(number*random_number)%26: number for number in NUMBERS_FOR_LETTERS}
    return ''.join([NUMBERS_FOR_LETTERS.get(decode_key.get(ord(letter)-97)) for letter in r if letter.isalpha()])
        

