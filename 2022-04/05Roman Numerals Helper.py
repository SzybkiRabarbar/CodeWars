class RomanNumerals:
    
    def to_roman(val):
        numbers=[['','I','II','III','IV','V','VI','VII','VIII','IX'],
                ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
                ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
                ['','M','MM','MMM']]
        content=[numbers[i][int(num)] for i,num in enumerate(str(val)[::-1])]
        return ''.join(content[::-1])

    def from_roman(roman_num):
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
