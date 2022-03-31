'''
https://www.codewars.com/kata/5263c6999e0f40dee200059d/solutions/python
'''
from itertools import product

dykta = {
        '1':['1','2','4'],
        '2':['2','1','3','5'],
        '3':['3','2','6'],
        '4':['4','1','5','7'],
        '5':['5','2','4','6','8'],
        '6':['6','3','5','9'],
        '7':['7','4','8'],
        '8':['8','5','7','9','0'],
        '9':['9','6','8'],
        '0':['0','8']
        }

def get_pins(observed):
    posibilities = [dykta[ob] for ob in observed]
    temp = ', '.join([str(posibilities[i]) for i in range(len(posibilities))])
    content = list(product(eval(temp)))
    return exec(temp)


def get_pins1(observed):
    content = []
    posibilites = [dykta[observed[i]] for i in range(len(observed))]
    code_len = len(posibilites)
    for num1 in posibilites[0]:
        if len(posibilites)==1:
            content.append(num1)
        else:
            for num2 in posibilites[1]:
                if len(posibilites)==2:
                    content.append(num1+num2)
                else:
                    for num3 in posibilites[2]:
                        if len(posibilites)==3:
                            content.append(num1+num2+num3)
                        else:
                            for num4 in posibilites[3]:
                                if len(posibilites)==4:
                                    content.append(num1+num2+num3+num4)
                                else:
                                    for num5 in posibilites[4]:
                                        if len(posibilites)==5:
                                            content.append(num1+num2+num3+num4+num5)
                                        else:
                                            for num6 in posibilites[5]:
                                                if len(posibilites)==6:
                                                    content.append(num1+num2+num3+num4+num5+num6)
                                                else:
                                                    for num7 in posibilites[6]:
                                                        if len(posibilites)==7:
                                                            content.append(num1+num2+num3+num4+num5+num6+num7)
                                                        else:
                                                            for num8 in posibilites[7]:
                                                                content.append(num1+num2+num3+num4+num5+num6+num7+num8)   
    return content      

print(get_pins('12'))
