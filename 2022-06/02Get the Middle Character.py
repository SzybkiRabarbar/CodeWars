# https://www.codewars.com/kata/56747fd5cb988479af000028/python
def get_middle(str):
    n = len(str)//2
    if len(str)%2==0:
        return str[n-1:n+1]
    return str[n]