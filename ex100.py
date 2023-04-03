from random import randint
from time import sleep
numeros = []
def sorteio():
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print('Sorteando os 5 valores da lista: ', end=' ')
    for n in numeros:
        print(n, end=' ')
        sleep(0.5)
    print('...pronto!')

def somapar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos valores pares existentes em {numeros} é {soma}')


sorteio()
somapar()
