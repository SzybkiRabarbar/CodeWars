#https://www.codewars.com/kata/626d691649cb3c7acd63457b/python
def formula1(verstappen: int, events: str) -> int:
    if f"{verstappen} I" in events: return -1
    pos=[str(x) for x in range(1,21)]
    events=iter(events.split())
    for pilot in events:
        event=next(events)
        if event == 'O':
            indx=pos.index(pilot)
            pos.insert(indx-1, pos.pop(indx))
        if event == 'I':
            pos.pop(pos.index(pilot)) 
    return pos.index(str(verstappen))+1

i1, i2 = 20, "9 O 17 O 9 O 12 O 2 O 12 O 9 O 1 O 5 O 12 O 17 O 20 O 16 O 7 O 2 O 8 O 16 O 14 O 3 I 14 O 11 O 16 O 1 I 13 O 8 O 14 O 5 I 12 O 4 O"
print(formula1(i1,i2))
