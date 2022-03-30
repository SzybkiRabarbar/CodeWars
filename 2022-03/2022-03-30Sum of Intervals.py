'''
https://www.codewars.com/kata/52b7ed099cdc285c300001cd/python
'''
def sum_of_intervals(intervals):
    content = []
    for inter in intervals:
        for i in range(inter[0],inter[1]):
            content.append(i)
    return len(list(set(content)))

print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))