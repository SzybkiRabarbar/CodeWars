'''
https://www.codewars.com/kata/5855777bb45c01bada0002ac/python
'''

colors = ['black','brown','red','orange','yellow','green','blue','violet','gray','white']
def encode_resistor_colors(ohms_string):
    ohms_string = ohms_string.split()
    ohms_string = ohms_string[0]
    ohms_string.strip()
    if ohms_string.endswith('k'): 
        ohms_string = ohms_string.replace('k','000')
    if ohms_string.endswith('M'): 
        ohms_string = ohms_string.replace('M','000000') 
    if ohms_string[1] == '.':
        ohms_string = ohms_string.replace('.','') 
        ohms_string = ohms_string.replace('0','',1)
    result = str()
    zeros = 0
    for indx,num in enumerate(ohms_string):
        if indx <= 1:
            result += colors[int(num)] + ' ' 
        else:
            zeros +=1
    result += colors[zeros] + ' ' 
    return result + 'gold'

print(encode_resistor_colors("1.2M ohms"))
