#https://www.codewars.com/kata/537e18b6147aa838f600001b/python
def justify(text:str, width:int)->str:
    content,result,temp=[],[],str()
    for word in text.split():
        temp += f"{word} "
        if (len(temp)-1)>width: 
            content.append(content_temp.strip())
            temp=f"{word} "
            content_temp=temp
        else:
            content_temp=temp
    
    for line in content:
        space=width-len(line.replace(' ',''))
        gaps=line.count(' ')
        if not gaps:
            result.append(line)
            continue
        division=space//gaps
        mod=space%gaps
        temp=str()
        for word in (line.split()):
            if mod:
                temp+=f"{word}{' '*division}{' '}"
                mod-=1
            else:
                temp+=f"{word}{' '*division}"
        result.append(temp.strip())
    result.append(content_temp.strip())
    return '\n'.join(result)
