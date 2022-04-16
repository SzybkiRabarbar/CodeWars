#https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
def order(sentence:str):
    sentence=[word for word in sentence.split()]
    content =[]
    for word in sentence[:]:
        for letter in word:
          if letter.isnumeric():
            content.append([letter,word])
            break
    content.sort()
    return ' '.join([x[1] for x in content])

print(order('is2 Thi1s T4est 3a'))