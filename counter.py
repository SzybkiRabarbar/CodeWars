from os import listdir
from os.path import isfile
from time import sleep

def ile_roz():
    return len([name for name in listdir('.') if isfile(name) and '.py' in name and not '000test.py' in name and not 'counter.py' in name])

def nadpis():
    readme = open('README.md','w')
    tresc = '# CodeWars <br/>\n' \
            'Mój profil na stronie Codewars <br/>\n' \
            '# https://www.codewars.com/users/NieetycznyPa%C5%BAdzierz%20 <br/>\n' \
            'Liczba zadań na tym repozytorium: '+str(ile_roz())                    
    readme.write(tresc)

while True:
    nadpis()
    sleep(3600)