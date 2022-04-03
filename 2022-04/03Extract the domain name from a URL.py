'''
https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
'''

def domain_name(url):
    url = url.replace('www.','').replace('http://','').replace('https://','')
    temp = url.split('/')
    domain = temp[0].split('.')
    return domain[0]

print(domain_name('https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python'))