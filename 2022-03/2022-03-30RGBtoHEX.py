'''
https://www.codewars.com/kata/513e08acc600c94f01000001/python
'''

def rgb(r, g, b):
    if r<0:
        r='00'
    elif r>255:
        r='ff'
    else:    
        r = hex(r)[2:]
        if len(r)==1:
            r = '0'+r
            
    if g<0:
        g='00'
    elif g>255:
        g='ff'
    else:    
        g = hex(g)[2:]
        if len(g)==1:
            g = '0'+g

    if b<0:
        b='00'
    elif b>255:
        b='ff'
    else:    
        b = hex(b)[2:]
        if len(b)==1:
            b = '0'+b           
    return r.upper()+g.upper()+b.upper()