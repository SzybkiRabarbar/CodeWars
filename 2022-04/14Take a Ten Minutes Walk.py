'''
https://www.codewars.com/kata/54da539698b8a2ad76000228/python
'''
def is_valid_walk(walk):
    if not len(walk)==10: return False
    horizontal,vertical=0,0
    for d in walk:
        if d=='n': vertical+=1
        if d=='s': vertical-=1
        if d=='e': horizontal+=1
        if d=='w': horizontal-=1
    if horizontal!=0 or vertical!=0: return False
    return True
