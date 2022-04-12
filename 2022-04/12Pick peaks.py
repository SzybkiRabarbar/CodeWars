'''
https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/python
'''
from itertools import takewhile

def pick_peaks(arr):
    pos=[]
    peaks=[]
    for indx, height in enumerate(arr):
        if indx==0 or indx==len(arr)-1: continue
        if height>arr[indx-1] and height>=arr[indx+1]:
            if height==arr[indx+1] and all([True if x==height else False for x in arr[indx:]]): continue
            if height==arr[indx+1] and any([True if x!=height else False for x in list(takewhile(lambda x: x>=height, arr[indx:]))]): continue   
            pos.append(indx)
            peaks.append(height)
    return {'pos':pos, 'peaks':peaks}
