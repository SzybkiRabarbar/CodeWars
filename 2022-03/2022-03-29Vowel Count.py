def get_count1(sentence):
    bad = ['a','e','i','o','u']
    n = 0
    for s in sentence:
        for b in bad:
            if b == s:
                n+=1
    return n

vo = ['a','e','i','o','u']
def get_count(sentence):
    return len([1 for s in sentence if [True for v in vo if v==s]])
