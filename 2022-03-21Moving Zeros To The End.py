def move_zeros(array):
    zeros = [z for z in array if not z]
    array = [arr for arr in array if arr]
    return array + zeros

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))