'''
https://www.codewars.com/kata/550f22f4d758534c1100025a/python
'''

def dirReduc(arr):
    for indx, direction in enumerate(arr):
        if indx+1 == len(arr): return arr
        if direction == "NORTH" and arr[indx+1] == "SOUTH": 
            arr.pop(indx)
            arr.pop(indx)
            dirReduc(arr)
        if direction == "SOUTH" and arr[indx+1] == "NORTH":
            arr.pop(indx)
            arr.pop(indx)
            dirReduc(arr)
        if direction == "EAST" and arr[indx+1] == "WEST":
            arr.pop(indx)
            arr.pop(indx)
            dirReduc(arr)
        if direction == "WEST" and arr[indx+1] == "EAST":
            arr.pop(indx)
            arr.pop(indx)
            dirReduc(arr)
    return arr

print(dirReduc(["EAST"]))
    
