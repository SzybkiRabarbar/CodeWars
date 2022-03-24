'''
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python
'''

def likes(names):
    end_sentence = [
        'no one likes this',
        ' likes this',
        ' like this',
        ' others like this'
    ]
    if not names: return end_sentence[0]
    if len(names) == 1:
        sentence = names[0]+end_sentence[1]
    elif len(names) == 2:
        sentence = names[0]+' and '+names[1]+end_sentence[2]
    elif len(names) == 3:
        sentence = names[0]+', '+names[1]+' and '+names[2]+end_sentence[2]
    else:
        sentence = names[0]+', '+names[1]+' and '+str(len(names)-2)+end_sentence[3]
    return sentence




