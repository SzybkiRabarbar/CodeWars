'''
https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python
'''
def solution(roman_num):
        trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        trans_lst, content, temp=[], 0, 0
        for roman_letter in roman_num:
            trans_lst.append(trans.get(roman_letter))
        for i,value in enumerate(trans_lst):
            if temp!=0:                 
                if i+1==len(trans_lst):
                    content+=temp
                    temp=0
                    continue
                
                if temp < trans_lst[i+1]:
                    temp = trans_lst[i+1] - temp
                    continue
                else:
                    content+=temp
                    temp=0
                    continue

            if i+1==len(trans_lst):
                content+=value
                continue

            if value < trans_lst[i+1]:
                temp = trans_lst[i+1] - value
            else:
                content+=value            
        return content