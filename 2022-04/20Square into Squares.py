import math
def decompose(n):
    content=[n-1]
    n_square = n*n - (n-1)*(n-1)    
    while n_square:
        temp=int(math.sqrt(n_square))
        content.append(temp)
        n_square-=temp*temp

print(decompose(10))