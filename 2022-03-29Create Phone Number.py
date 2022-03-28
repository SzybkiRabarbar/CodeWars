'''
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
'''
def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))