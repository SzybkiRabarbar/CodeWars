'''
https://www.codewars.com/kata/5d076515e102162ac0dc514e/python
'''
t=['Baby shark','Mommy shark','Daddy shark','Grandma shark','Grandpa shark',"Let's go hunt",'doo doo doo doo doo doo']
def baby_shark_lyrics():
    r=str()
    for i in range(6):
        for _ in range(3):
            r+=f"{t[i]}, {t[6]}\n"
        r+=f"{t[i]}!\n"
    return f"{r}Run away,…"

