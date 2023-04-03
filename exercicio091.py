from random import randint
from operator import itemgetter
from time import sleep
players = dict()
ranking = list()
players['player1'] = randint(1, 6)
players['player2'] = randint(1, 6)
players['player3'] = randint(1, 6)
players['player4'] = randint(1, 6)
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)

for k, i in players.items():
    sleep(1)
    print(f'{k} -> {i}')

print('Ranking: ')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}st place -> {v[0]} with {v[1]}')




