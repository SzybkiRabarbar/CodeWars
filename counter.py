from os import listdir
from os.path import isdir
from time import sleep
from subprocess import run

ignore = ['000test.py', 'counter.py']

def ile_roz():
    content=0
    for dir in listdir('.'):
        if isdir(dir):
            content += len([name for name in listdir(dir) if '.py' in name and not name in ignore])
    return content

def nadpis():
    readme = open('README.md','w')
    tresc = '# CodeWars <br/>\n' \
            'Mój profil na stronie Codewars <br/>\n' \
            '# https://www.codewars.com/users/NieetycznyPa%C5%BAdzierz%20 <br/>\n' \
            'Liczba rozwiązań na tym repozytorium: '+str(ile_roz())                    
    readme.write(tresc)

def push_to_git():
    run(['git', 'add', '.'])
    run(['git', 'commit', '-m', 'Wysłane automatycznie', '.'])
    run(['git', 'push', 'https://github.com/SzybkiRabarbar/CodeWars.git'])

if __name__ == '__main__':
    nadpis()
    push_to_git()
'''

Komendy do zatrzymania programu w tle:
# ps aux | grep 'counter.py'
# kill PID

'''