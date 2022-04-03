'''
https://www.codewars.com/kata/523a86aa4230ebb5420001e1/python
'''
def anagrams2(word, words):
    return [word_from_lst for word_from_lst in words if sorted(word_from_lst)==sorted(word)]

def anagrams1(word, words):
    content=[]
    for word_from_lst in words:
        if sorted(word_from_lst)==sorted(word): content.append(word_from_lst)
    return content
print(anagrams2('abba', ['aabb', 'abcd', 'bbaa', 'dada']))