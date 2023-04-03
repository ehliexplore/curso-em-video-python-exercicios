from random import randint
from time import sleep
numbers = []
def sorteio():
    for c in range(0, 5):
        numbers.append(randint(0, 10))
    print('Sorteando...')
    for n in numbers:
        print(n, end=' ')
        sleep(0.5)
    print('Pronto!')

def somapar():
    soma = 0
    for n in numbers:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos números pares em {numbers} é {soma}')


sorteio()
somapar()

