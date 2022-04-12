from math import ceil
MORSE_CODE_DICT = {'.-': 'A',
                   '-...': 'B', 
                   '-.-.': 'C', 
                   '-..': 'D', 
                   '.': 'E', 
                   '..-.': 'F', 
                   '--.': 'G', 
                   '....': 'H', 
                   '..': 'I', 
                   '.---': 'J', 
                   '-.-': 'K', 
                   '.-..': 'L', 
                   '--': 'M', 
                   '-.': 'N', 
                   '---': 'O', 
                   '.--.': 'P', 
                   '--.-': 'Q', 
                   '.-.': 'R', 
                   '...': 'S', 
                   '-': 'T', 
                   '..-': 'U', 
                   '...-': 'V', 
                   '.--': 'W', 
                   '-..-': 'X', 
                   '-.--': 'Y', 
                   '--..': 'Z', 
                   '.----': '1', 
                   '..---': '2', 
                   '...--': '3', 
                   '....-': '4', 
                   '.....': '5', 
                   '-....': '6', 
                   '--...': '7', 
                   '---..': '8', 
                   '----.': '9', 
                   '-----': '0', 
                   '--..--': ', ', 
                   '.-.-.-': '.', 
                   '..--..': '?', 
                   '-..-.': '/', 
                   '-....-': '-', 
                   '-.--.': '(',
                   '-.--.-': ')',
                   '-.-.--': '!',
                   '0': ' ',
                   '...---...': 'SOS'
                   }

def decodeMorse(morse_code:str):
    morse_code = morse_code.replace('   ', ' 0 ')
    morse_code = ''.join([MORSE_CODE_DICT.get(code) for code in morse_code.split()])
    return morse_code.strip()

def decodeBitsAdvanced(bits:str):
    bits_lst, max_1, max_0 = bits_to_list(bits)
    if len(bits_lst)==1: return '.'
    max_len = max_1 if max_1>max_0 else max_0
    morse_code = str()
    for bit in bits_lst:
        if '1' in bit:
            if len(bit)>=ceil(max_len/2):
                morse_code+='-'
            else:
                morse_code+='.'

        if '0' in bit:
            if len(bit)>=ceil(max_len/2):
                morse_code+='   '
            elif len(bit)>=ceil(max_len/6):
                morse_code+=' '
            else:
                morse_code+=''
    return morse_code

def bits_to_list(bits:str):
    bits = bits.strip('0')
    bits1 = [bit for bit in bits.split('0') if bit]
    bits0 = [bit for bit in bits.split('1') if bit]
    bits_lst=[]
    for i in range(len(bits1)):
        if not i:
            bits_lst.append(bits1[i])
        else:
            bits_lst.append(bits0[i-1])
            bits_lst.append(bits1[i])
    try:
        max_1 = len(max(bits1))
    except ValueError: 
        max_1 = 0
    try:
        max_0 = len(max(bits0))
    except ValueError: 
        max_0 = 0              
    return bits_lst, max_1, max_0


b= '0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000' #HEY JUDE
print(decodeMorse(decodeBitsAdvanced(b))) 

