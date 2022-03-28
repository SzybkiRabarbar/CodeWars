def create_phone_number(n):
    first = "".join(n[:3])
    return '('+first

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))