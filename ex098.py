from time import sleep

def linha():
    print('=' * 40)

def counter(i, f, p):
    linha()
    print(f'Contando de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    cont = i
    if f > i:
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont += p
        print('FIM.')
    else:
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont -= p
        print('FIM.')


counter(1, 10, 1)
counter(10, 1, 2)
linha()
print('Agora é a sua vez de personalizar.')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
counter(ini, fim, pas)







