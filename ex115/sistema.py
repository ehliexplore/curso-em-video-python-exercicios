from lib.interface import *
from lib.arquivo import *
from time import sleep

file = ('cursoemvideo.txt')
if not fileExist(file):
    createFile(file)


while True:
    answer = menu(['See registered people', 'Register new person', 'Exit'])
    if answer == 1:
        readFile(file)
    elif answer == 2:
        name = str(input('Name: '))
        age = integer('Age: ')
        register(file, name, age)
    elif answer == 3:
        header(f'Finishing...')
        break
    else:
        print('\033[31mERROR. select a valid option.\033[m')
    sleep(1)







