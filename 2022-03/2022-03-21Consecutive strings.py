'''
https://www.codewars.com/kata/56a5d994ac971f1ac500003e/python
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
'''

def longest_consec(strarr, k):
    if len(strarr) == 0 or len(strarr) < k or k <= 0: return ""
    consec_list = []
    for i, st in enumerate(strarr):
        iplus = i+1
        content = st
        for kk in range(k-1):
            try:
                content += strarr[iplus]
                iplus += 1
            except IndexError:
                continue
        consec_list.append(content)
    consec_list.sort(reverse=True,key=len)
    return consec_list[0]



print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
    
