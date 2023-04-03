person = dict()
group = list()
ages = 0
while True:
    person.clear()
    person['name'] = str(input('Name: '))
    person['age'] = int(input('Age: '))
    person['sex'] = str(input('Sex [M/F]: ')).upper().strip()[0]
    ages += person['age']
    answer = str(input('Want to continue? [Y/N]: ')).upper().strip()[0]
    group.append(person.copy())
    if answer == 'N':
        break

average = ages / len(group)
print(group)
print('={[][=}}' * 5)
print(f'{len(group)} people registered.')
print('={[][=}}' * 5)
print(f'The average age is {average}')
print('={[][=}}' * 5)
print(f'The womans are: ')
for i, v in enumerate(group):
    if v['sex'] == 'F':
        print(v['name'])
print('={[][=}}' * 5)
print('Above-average people are: ')
for i, v in enumerate(group):
    if v['age'] > average:
        print(v['name'])
print('===========================================')








