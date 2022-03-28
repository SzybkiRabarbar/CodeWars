def create_phone_number(n):
    first =str()
    seccond =str()
    three =str()

    for i, num in enumerate(n):
        if i <= 2:
            first += str(num)
        elif i <= 5:
            seccond += str(num)
        else: 
            three += str(num)

    return '('+first+') '+seccond+'-'+three

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))