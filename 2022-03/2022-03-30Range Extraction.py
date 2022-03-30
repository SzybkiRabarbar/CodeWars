'''
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/python
'''

def solution(args):
    num_range =[]
    content = str()
    for indx, arg in enumerate(args):
        if indx+1 == len(args):
            if len(num_range)==1:
                content += str(num_range[0])+','+str(arg)
                break
            elif arg-1== args[indx-1]:
                content += str(num_range[0])+'-'+str(arg)
                break
            else:
                content+=str(arg)
                break
        
        if arg+1 == args[indx+1]:
            num_range.append(arg)
        elif len(num_range)==1:
            content += str(num_range[0])+','+str(arg)+','
            num_range =[]
        elif arg-1== args[indx-1]:
            content += str(num_range[0])+'-'+str(arg)+','
            num_range =[]
        else:
            content += str(arg)+','
    return content

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))

'''
def solution(args):
    num_range =[]
    content = str()
    for indx, arg in enumerate(args):
        if indx+1 == len(args):
            if len(num_range)==1:
                content += str(num_range[0])+','+str(arg)
                break
            elif arg-1== args[indx-1]:
                content += str(num_range[0])+'-'+str(arg)
                break
            else:
                content+=str(arg)
                break
        
        if arg+1 == args[indx+1]:
            num_range.append(arg)
        elif len(num_range)==1:
            content += str(num_range[0])+','+str(arg)+','
            num_range =[]
        elif arg-1== args[indx-1]:
            content += str(num_range[0])+'-'+str(arg)+','
            num_range =[]
        else:
            content += str(arg)+','
    return content
'''