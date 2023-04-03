matrix = [[], [], []]
for c in range(0, 3):
    matrix[0].append(int(input(f'Insert an value [0, {c}]: ')))
for c in range(0, 3):
    matrix[1].append(int(input(f'Insert an value [1, {c}]: ')))
for c in range(0, 3):
    matrix[2].append(int(input(f'Insert an value [2, {c}]: ')))

for c in range(0, 3):
    print(f'[  {matrix[0][c]: ^5}  ]', end='')
print()
for c in range(0, 3):
    print(f'[  {matrix[1][c]: ^5}  ]', end='')
print()
for c in range(0, 3):
    print(f'[  {matrix[2][c]: ^5}  ]', end='')
print()

sumpairs = 0
for c in range(0, 3):
    for n in matrix[c]:
        if n % 2 == 0:
            sumpairs = sumpairs + n
print(f'The sum of even values is {sumpairs}')
third_column = matrix[0][2] + matrix[1][2] + matrix[2][2]
print(f'The sum of the values in the third column is {third_column}')
print(f'The largest value of the second line is {max(matrix[1])}')







