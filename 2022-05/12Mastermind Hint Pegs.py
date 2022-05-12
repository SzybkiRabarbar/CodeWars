#https://www.codewars.com/kata/54f0d905d49112f3a300055a/python
def get_hints(answer:list, guess:list)->dict:
    result = {'black':0, 'white':0}
    for i,g in enumerate(guess[:]):
        if answer[i]==g:
            result['black'] = result.get('black')+1
            answer[i] = ''
            guess[i] = ''
    for i,g in enumerate(guess[:]):
        if g=='': continue
        if g in answer:
            result['white'] = result.get('white')+1
            answer[answer.index(g)] = ''
            guess[i] = ''
    return result
            