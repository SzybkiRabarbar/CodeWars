'''
https://www.codewars.com/kata/51c8e37cee245da6b40000bd/python
'''
def solution(string:str,markers):
    s_lst=string.split('\n')
    content = []
    for line in s_lst:
        find = False
        for mark in markers:
            if mark in line:
                find = True
                line = line.split(mark)[0]
                if [mark2 for mark2 in markers if mark2 in line]: continue
                content.append(line.strip())
        if find: continue
        content.append(line.strip())
    return '\n'.join(content)

print(solution("apples, pears # and bananas\ngrapes\nbananas !#apples", ["#", "!"]))
