def integer(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('Data entry was interrupted by the user.')
            return 0
        except (ValueError, TypeError):
            print('\033[31mInvalid. Insert an valid option.\033[m')
            continue
        else:
            return n


def linha():
    return '=' * 42


def header(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lst):
    header('\033[040mMENU PRINCIPAL\033[m')
    c = 1
    for items in lst:
        print(f'\033[33m{c} - \033[34m{items}\033[m')
        c += 1
    print(linha())
    while True:
        opc = integer('Select option: ')
        return opc

