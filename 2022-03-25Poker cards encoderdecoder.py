'''
https://www.codewars.com/kata/52ebe4608567ade7d700044a/python
'''

face = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suit = {'c':0, 'd':13, 'h':26, 's':39}

def encode(cards):
    return sorted([face.index(card[0])+suit[card[1]] for card in cards])

def decode(cards):
    content=[]
    for card in sorted(cards):
        if (card-39)>=0: #s
            content.append(face[card-39]+'s')
        elif (card-26)>=0: #h
            content.append(face[card-26]+'h')
        elif (card-13)>=0: #d
            content.append(face[card-13]+'d')
        else: #c
            content.append(face[card]+'c')
    return content

print(encode(["Qh", "Ac", "5h", "Ks"]))
print(decode([7, 22, 51]))