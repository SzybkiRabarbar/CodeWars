'''
https://www.codewars.com/kata/5270d0d18625160ada0000e4/python
'''
def score(dice:list):
    points_value = [0,1000,200,300,400,500,600]
    points=0
    dice.sort()
    for i,d in enumerate(dice):
        if dice.count(d)>=3 and d:
            points += points_value[d]
            dice[i],dice[i+1],dice[i+2]=0,0,0
        elif d==1 or d==5:
            points += int(points_value[d]/10)
    return points

