#https://www.codewars.com/kata/55f89832ac9a66518f000118/python
def poly_to_dict(poly:str)->list:
    content:dict={}
    for el in poly.replace('-',' -').replace('+',' +').split():
        temp_alpha=str()
        temp_rest=str()
        for digit in el:
            if digit.isalpha():
                temp_alpha+=digit
            else:
                temp_rest+=digit
        temp_alpha=''.join(sorted(temp_alpha))
        if not temp_rest.startswith('+') and not temp_rest.startswith('-'): temp_rest=f"+{temp_rest}"
        if len(temp_rest)==1: temp_rest+='1'
        temp_rest=int(temp_rest)
        if not temp_alpha in content:
            content[temp_alpha]=temp_rest
            continue
        x=content.get(temp_alpha)
        content.update({temp_alpha:x+temp_rest})
    return content
    #key=lambda x: (len(x), x)

def dict_to_str(poly_dict:dict)->str:
    result=str()
    lst=[[key, item]for key, item in poly_dict.items()]
    lst.sort(key=lambda x: (len(x[0]), x[0]))
    for el in lst:
        if el[1]==0: continue
        if el[1]==1:
            result+=f"+{el[0]}"
            continue
        if el[1]==-1:
            result+=f"-{el[0]}"
            continue
        if el[1]<-1:
            result+=f"{el[1]}{el[0]}"
            continue
        if el[1]>1:
            result+=f"+{el[1]}{el[0]}"
            continue
    if result.startswith('+'): result=result.replace('+','',1)
    return result
        
    
def simplify(poly:str)->str:
    print(poly)
    poly_dict=poly_to_dict(poly)
    return dict_to_str(poly_dict)


#print(simplify("2xy-yx"))