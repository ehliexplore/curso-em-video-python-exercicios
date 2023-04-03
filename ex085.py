numbers = [[], []]
for c in range(0, 7):
    n = int(input(f'Enter a number ({c}): '))
    if n % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)
print(numbers)
print(f'The pairs numbers are {sorted(numbers[0])}.')
print(f'The odds numbers are {sorted(numbers[1])}')




