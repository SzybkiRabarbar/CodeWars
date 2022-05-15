#https://www.codewars.com/kata/576b072359b1161a7b000a17/python
def generate_pascal_triangle(layers:int)->list:
    if layers == 0: return []
    if layers == 1: return [[1]]
    triangle = [[1],[1,1]]
    if layers == 2: return triangle
    for i in range(2,layers):
        temp = [(triangle[-1][indx]+triangle[-1][indx-1]) for indx in range(1,i)]
        temp.insert(0,1)
        temp.append(1)
        triangle.append(temp)
    return triangle

def generate_diagonal(n:int, l:int)->list:
    triangle = generate_pascal_triangle(n+l)
    return [triangle[n+i][n] for i in range(l)]