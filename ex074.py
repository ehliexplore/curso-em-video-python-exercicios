from random import randint

sorteio = (randint(0, 10), randint(0, 10), randint(0,10),
           randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end=' ')
for c in sorteio:
    print(c, end=' ')
print()
print(f'O mair número é {max(sorteio)} e o menor número é {min(sorteio)}.')
