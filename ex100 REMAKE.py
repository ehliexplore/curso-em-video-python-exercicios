from random import randint
numbers = list()


def random():
    for c in range(0, 5):
        numbers.append(randint(0, 10))
    print('The numbers drawn are: ', end=' ')
    for n in numbers:
        print(f'{n}', end=' ')


def sum():
    soma = 0
    for n in numbers:
        if n % 2 == 0:
            soma += n
    print(f'\nThe sum of the even numbers is: {soma}')


random()
sum()
