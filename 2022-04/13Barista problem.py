def barista(coffees:list):
    coffees.sort()
    sus_wait_time=[]
    waiting_time=0
    for i,coffe in enumerate(coffees):
        waiting_time+=coffe
        if i: waiting_time+=2
        sus_wait_time.append(waiting_time)
    return sum(sus_wait_time)