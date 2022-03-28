'''
https://www.codewars.com/kata/55f5efd21ad2b48895000040/solutions/python
'''

def max_sumDig(nMax, maxSum):
    numb_lst = []
    for numb in range(1000,nMax+1):
        is_numb_valid = 0
        is_numb_valid1 = 0
        is_numb_valid2 = 0
        if numb > 9999:
            for num in str(numb)[:4]:
                is_numb_valid1 += int(num)
            for num in str(numb)[1:]:
                is_numb_valid2 += int(num)
            if is_numb_valid1 <= maxSum and is_numb_valid2 <= maxSum:
                numb_lst.append(numb)
        else:
            for num in str(numb):
                is_numb_valid += int(num)
            if is_numb_valid <= maxSum: 
                numb_lst.append(numb)

    content1 = len(numb_lst)
    content3 = sum(numb_lst)
    mean = content3/content1
    close_to_mean = [abs(i-mean) for i in numb_lst]
    content2 = numb_lst[close_to_mean.index(min(close_to_mean))]
    return [content1, content2 ,content3]

print(max_sumDig(35644, 9))