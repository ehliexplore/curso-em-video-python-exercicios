def line():
    return '~' * 42


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(lst):
    header('MAIN MENU NAME&AGE SYSTEM')
    cont = 1
    for a in lst:
        print(f'\033[33m{cont}\033[m - \033[34m{a}\033[m')
        cont += 1
    print(line())
    opc = integer('Select an option: ')
    return opc


def integer(msg):
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print('Invalid option.')
            continue
        else:
            return num
