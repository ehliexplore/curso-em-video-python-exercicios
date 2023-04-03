from lib.interface import *

def fileExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True



def createFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('There was an error creating the file.')
    else:
        print(f'File {name} successfully created.')


def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('Error while attempting to read file.')
    else:
        header('REGISTERED PEOPLE')
        for p in a:
            data = p.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<35}{data[1]:^3} years')
    finally:
        a.close()


def register(file, name='unknow', age=0):
    try:
        a = open(file, 'at')
    except:
        print('Error while attempting to read file.')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('There was an error while writing the data.')
        else:
            print(f'New person registered: {name}')
            a.close()


