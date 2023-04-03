def infos(h):
    help(q)


def title(t):
    print('=' * len(t))
    print(f'{t}')
    print('=' * len(t))


q = ''
while True:
    print('\033[0;36;40m=' * 21)
    print(f'  DOCSTRINGS PYTHON')
    print(21 * '=')
    print('\033[m')
    q = str(input('HELP: ')).lower().strip()
    print('\033[1;30;43m')
    if q == 'sair':
        print('PROGRAM FINALIZADO.')
        break
    else:
        title(q)
        infos(q)


