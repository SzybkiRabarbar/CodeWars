'''
https://www.codewars.com/kata/52449b062fb80683ec000024/python
'''
def generate_hashtag(s):
    if not s: return False
    words=s.title().split()
    content = '#'+''.join(words)
    if len(content)>140: return False
    return content

print(generate_hashtag('  dzien dobry polsko'))