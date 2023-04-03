def players(a='<unknown>', b=0):
    return f'The player {a} did {b} points on the game.'


name = str(input('Name: '))
points = str(input('Points: '))
if points.isnumeric():
    points = int(points)
else:
    points = 0
if name.strip() == '':
    print(players(b=points))
else:
    print(players(name, points))








