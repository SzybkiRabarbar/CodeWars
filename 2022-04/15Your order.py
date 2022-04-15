#https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
def order(sentence):
  sentence=[[w for w in word if w.isnumeric()],word for word in sentence]
  return sentence