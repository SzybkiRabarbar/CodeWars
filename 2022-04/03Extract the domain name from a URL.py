def domain_name(url):
    url = url.replace('http://','')
    url = url.replace('https://','')
    return url

print(domain_name('http://github.com/carbonfive/raygun'))