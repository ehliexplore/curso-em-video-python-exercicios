students = list()
cont = 0
while True:
    name = str(input('Name: '))
    grade1 = float(input('First grade: '))
    grade2 = float(input('Second grade: '))
    average = (grade1 + grade2) / 2
    students.append([name, [grade1, grade2], average])
    cont += 1
    answer = str(input('Wanto to continue? [Y/N]: ')).upper().strip()[0]
    if answer == 'N':
        break

print(students)
print(f'{"No.":<4}{"NAME":<10}{"AVERAGE":>8}')
for i, v in enumerate(students):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8}')

while True:
    menu = int(input('Do you want to see the grades of which student? (exit: 999): '))
    if menu == 999:
        break
    elif menu < cont:
        print(f'{students[menu][0]} -> GRADES: {students[menu][1][0]} and {students[menu][1][1]}')
    else:
        print('Student dont find. Enter another number.')












