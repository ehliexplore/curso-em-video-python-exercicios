from random import randint
from time import sleep
games = []
ticket = []
amount = int(input('Amount of tickets: '))
total = 0
while total < amount:
    ticket.clear()
    while len(ticket) < 6:
        number = randint(1, 60)
        if number not in ticket:
            ticket.append(number)
    ticket.sort()
    games.append(ticket[:])
    total += 1
for i, v in enumerate(games):
    print(f'{i+1} -> {v}')
    sleep(0.5)





