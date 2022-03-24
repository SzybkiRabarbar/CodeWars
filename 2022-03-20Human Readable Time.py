'''
https://www.codewars.com/kata/52685f7382004e774f0001f7/python
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

'''

def make_readable(seconds:int):
    ss = seconds%60
    mm = (int((seconds-ss)/60))%60
    hh = (int((seconds-mm)/3600)) 
    if ss <=9: ss = '0'+str(ss)
    if mm <=9: mm = '0'+str(mm)
    if hh <=9: hh = '0'+str(hh)
    return str(hh)+':'+str(mm)+':'+str(ss)

'''
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
'''

print(make_readable(21000))