def tunnel_digging(r):
    ROCKS = {'[':30,']':30,
             '{':25,'}':25,
             '(':20,')':20,
             '|':15,':':10,
             ' ':0}
    time=30*(len(r)//3)
    print(time)
    for section in r:
        for rock in section:
            time+=ROCKS.get(rock)
    return time

print(tunnel_digging(['(]', '  ', '|}', ' ', ' ', '  ']))