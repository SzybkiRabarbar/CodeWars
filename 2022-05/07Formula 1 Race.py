#https://www.codewars.com/kata/626d691649cb3c7acd63457b/python
def champion_rank(verstappen: int, events: str) -> int:
    if f" {verstappen} I" in events: return -1
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
