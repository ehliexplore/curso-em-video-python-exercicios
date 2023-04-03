group = []
people = []
heaviest = 0
lightest = 0
while True:
    people.clear()
    people.append(str(input('Name: ')))
    people.append(int(input('Weight: ')))
    if len(group) == 0:
        heaviest = lightest = people[1]
    else:
        if people[1] > heaviest:
            heaviest = people[1]
        if people[1] < lightest:
            lightest = people[1]
    group.append(people[:])
    answer = str(input('Continue? [Y/N]: ')).upper().strip()[0]
    if answer == 'N':
        break
print(group)
print(f'{len(group)} people were registered.')
print(f'The heaviest person is', end=' ')
for p in group:
    if p[1] == heaviest:
        print(p[0])
print(f'The lightest person is', end=' ')
for p in group:
    if p[1] == lightest:
        print(p[0])




