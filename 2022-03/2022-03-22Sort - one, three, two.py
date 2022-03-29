'''
https://www.codewars.com/kata/56f4ff45af5b1f8cd100067d/solutions
'''
def sort_by_name(arr):
    unit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teen = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    ten = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    content = []
    result = []
    for ar in arr:
        if ar<10:
            content.append(unit[ar])
        elif ar>=10 and ar<=19:
            content.append(teen[ar-10])
        elif ar>19 and ar<=99:
            content_nt_nn = str()
            if ar%10 == 0:
                content_nt_nn = ten[int(str(ar)[0])]
            else:
                content_nt_nn = ten[int(str(ar)[0])] + '-' + unit[int(str(ar)[1])]
            content.append(content_nt_nn)
        else:
            content_hund = str()
            if ar%100 == 0:
                content_hund += unit[int(str(ar)[0])] + ' hundred'
            elif ar%10 == 0:
                content_hund += unit[int(str(ar)[0])] + ' hundred and ' + ten[int(str(ar)[1])]
            else:
                content_hund += unit[int(str(ar)[0])] + ' hundred and ' + ten[int(str(ar)[1])] + '-' + unit[int(str(ar)[2])]
            content.append(content_hund)
    for ind in range(len(arr)):
        result.append([arr[ind] ,content[ind]])
    result.sort(key=lambda x: x[1])
    return [r[0] for r in result]

print(sort_by_name([1, 2, 3, 4, 50, 57]))




