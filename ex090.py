student = {}
student['name'] = str(input('Name: '))
student['grade'] = float(input(f'{student["name"]}s grade: '))
if student['grade'] >= 7:
    student['situation'] = 'aproved'
elif 4 <= student['grade'] < 7:
    student['situation'] = 'recuperation'
else:
    student['situation'] = 'reproved'

for k, v in student.items():
    print(f'{k} is {v}')
