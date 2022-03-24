'''
https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/python
In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 
'''

def wave(people):
    content = []
    for i ,person in enumerate(people):
        people_e = [p for p in people]
        people_e.pop(i)
        people_e.insert(i ,person.upper())
        people_e = ''.join(people_e)
        if people_e.islower(): continue
        content.append(people_e)
    return content

print(wave('hello piwo'))

'''
def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
'''

