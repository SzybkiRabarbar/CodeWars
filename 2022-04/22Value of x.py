'''
https://www.codewars.com/kata/614ac445f13ead000f91b4d0/python
'''
def solve(eq: str):
    eq = eq.split('=')
    e_left, e_right = eq[0].split(), eq[1].split()
    left, right = 0, 0
    for i,e in enumerate(e_left):
        if not e.isnumeric(): continue
        if i-1>=0 and e_left[i-1]=="-":
            left-=int(e)
        else:
            left+=int(e)
    for i,e in enumerate(e_right):
        if not e.isnumeric(): continue
        if i-1>=0 and e_right[i-1]=="-":
            right-=int(e)
        else:
            right+=int(e)
    if 'x' in e_left:
        if e_left.index('x')-1>=0 and e_left[e_left.index('x')-1]=='-':
            return left-right
        return right-left
    else:
        if e_right.index('x')-1>=0 and e_right[e_right.index('x')-1]=='-':
            return right-left
        return left-right


