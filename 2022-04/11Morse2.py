'''
https://www.codewars.com/kata/54b72c16cd7f5154e9000457/python
'''
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

def decode_morse(morse_code:str):
    morse_code = morse_code.replace('   ', ' 0 ')
    morse_code = ''.join([MORSE_CODE_DICT.get(code) for code in morse_code.split()])
    return morse_code.strip()

def decode_bits(bits:str):
    time = time_unit(bits.strip('0'))
    bits = ''.join([b for i,b in enumerate(bits)if i%time==0])
    morse_code = bits.replace('0000000','   ').replace('000',' ').replace('111','-').replace('0','').replace('1','.')
    return morse_code

def time_unit(bits:str):
    time_lst1 = [len(t) for t in str(bits).split('0') if t]
    time_lst0 = [len(t) for t in str(bits).split('1') if t]
    if not time_lst0: return min(time_lst1)
    if min(time_lst0)<min(time_lst1): return min(time_lst0)
    return min(time_lst1)

if __name__ == '__main__':
    b = '0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000'
    print(decode_morse(decode_bits(b)))

