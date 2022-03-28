from os import listdir
from os.path import isfile
from time import sleep
from subprocess import run

def ile_roz():
    return len([name for name in listdir('.') if isfile(name) and '.py' in name and not '000test.py' in name and not 'counter.py' in name])

def nadpis():
    readme = open('README.md','w')
    tresc = '# CodeWars <br/>\n' \
            'Mój profil na stronie Codewars <br/>\n' \
            '# https://www.codewars.com/users/NieetycznyPa%C5%BAdzierz%20 <br/>\n' \
            'Liczba zadań na tym repozytorium: '+str(ile_roz())                    
    readme.write(tresc)

def push_to_git():
    run(['git', 'add', '.'])
    run(['git', 'commit', '-m', '"Wysłane automatycznie"', '.'])
    run(['git', 'push', 'origin', 'master'])
#
#while True:
#    nadpis()
#    push_to_git()
#    sleep(3600)
#
if __name__ == '__main__':
    nadpis()
    push_to_git()

'''

Komendy do zatrzymania programu w tle:
# ps aux | grep 'counter.py'
# kill PID

'''