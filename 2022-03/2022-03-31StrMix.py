'''
https://www.codewars.com/kata/5629db57620258aa9d000014/python
'''
def mix(s1, s2):
    dict1, dict2 = {}, {}
    lst_letter1 = [s for s in s1 if ord(s)<=122 and ord(s)>=97]
    lst_letter2 = [s for s in s2 if ord(s)<=122 and ord(s)>=97]
    
    for letter in lst_letter1:
        if letter in dict1: continue
        count_letter = lst_letter1.count(letter)
        if count_letter>1: dict1[letter] = count_letter

    for letter in lst_letter2:
        if letter in dict2: continue
        count_letter = lst_letter2.count(letter)
        if count_letter>1: dict2[letter] = count_letter 

    content = ['1:'+''.join([key for t in range(value)]) for key, value in dict1.items()]
    temp = ['2:'+''.join([key for t in range(value)]) for key, value in dict2.items()]
    
    sus = [c[-1] for c in content]
    
    for t in temp:
        if t[-1] in sus:
            indx = sus.index(t[-1])
            if len(t)>len(content[indx]):
                content.pop(indx)
                content.insert(indx,t)
            elif len(t)==len(content[indx]):
                new = content[indx].replace('1','=')
                content.pop(indx)
                content.insert(indx,new)
        else:
            content.append(t)
    
    content.sort(key=lambda x:(-len(x), x))
    return '/'.join(content)
print(mix("=qq dedede bbbbbbb", "qqq b dedede b bbbb #@"))
        