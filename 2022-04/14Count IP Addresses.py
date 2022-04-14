'''
https://www.codewars.com/kata/526989a41034285187000de4/train/python
'''
#Biblioteka ipaddress 

def ips_between(start, end):
    start_lst=[int(s) for s in start.split('.')]
    end_lst=[int(s) for s in end.split('.')]
    content = [end_lst[i]-start_lst[i] for i in range(4)]
    content[0]=content[0]*(256**3)
    content[1]=content[1]*(256**2)
    content[2]=content[2]*(256)
    
    return sum(content)

