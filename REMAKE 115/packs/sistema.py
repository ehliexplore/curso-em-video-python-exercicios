from interface import *
from arquivo import *
from time import sleep

file = ('cursoemvideo.txt')
if not fileExist(file):
    criarFile(file)

while True:
    sleep(1)
    answer = menu(['See registered people', 'Register new person', 'Exit'])
    if answer == 1:
        readFile(file)
    elif answer == 2:
        name = str(input('Name: '))
        age = integer('Age: ')
        register(file, name, age)
    elif answer == 3:
        print('Finishing...')
        break
    else:
        print('Invalid option.')



