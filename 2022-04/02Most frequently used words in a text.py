'''
https://www.codewars.com/kata/51e056fe544cf36c410000fb/python
'''

def top_3_words(text):
    new_text = str()
    dykta = {}
    for i, letter in enumerate(text):
        if letter.isalpha():
            new_text += letter.lower()
        else:
            if letter=="'" and (text[i-1].isalpha() or text[i+1].isalpha()):
                new_text += "'"
                continue
            new_text += ' '
    arr = new_text.split()

    for word in arr:
        if word in dykta: continue
        count = arr.count(word)
        dykta[word]=count

    dykta = list({k: v for k, v in sorted(dykta.items(), reverse=True, key=lambda item: item[1])}.keys())

    if len(dykta)>2:
        return [dykta[0], dykta[1], dykta[2]]
    elif len(dykta)==2:
        return [dykta[0], dykta[1]]
    elif len(dykta)==1:
        return [dykta[0]]
    else:
        return []

print(top_3_words("12412 mog0us"))