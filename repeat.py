player = dict()
player['name'] = str(input("Athlete's name: "))
player['gender'] = str(input("Athlete's gender [M/F/NB]: ")).upper().strip()
quantgames = int(input('How many games the athlete played? '))
points = []
for c in range(0, quantgames):
    points.append(int(input(f'Points on game {c}: ')))
player['points'] = points
player['total'] = sum(points)
print('///' * 20)
print(player)
print('///' * 20)
for i, v in enumerate(points):
    if player['gender'] == 'M':
        print(f'On the game {i} he made {v} points.')
    if player['gender'] == 'F':
        print(f'On the game {i}, she made {v} points.')
    if player['gender'] == 'NB':
        print(f'On the game {i}, they made {v} points.')
print(f'///' * 20)
for k, v in player.items():
    print(f'{k} : {v}')
print(f'The athlete played {quantgames} games.')
print('///' * 20)



