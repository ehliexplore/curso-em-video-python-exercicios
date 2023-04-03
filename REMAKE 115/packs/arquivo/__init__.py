from interface import *

def fileExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Theres was an error creating the file.')
    else:
        print(f'File {name} successfully created.')


def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('There are an error reading the file.')
    else:
        header('REGISTERED PEOPLE')
        for p in a:
            data = p.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} years')
    finally:
        a.close()


def register(arch, name='unknown', age=0):
    try:
        a = open(arch, 'at')
    except:
        print('There are an error reading the data.')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('There as an error while writing the data.')
        else:
            print(header(f'New person registered: {name}'))
            a.close()










