numbers = []
while True:
    n = int(input('Enter a value: '))
    if n not in numbers:
        numbers.append(n)
        print('Value added to the list.')
    else:
        print('Duplicate value. Will not be added to the list.')
    choice = str(input('Want to continue? [Y/N]: ')).upper().strip()[0]
    if choice == 'N':
        break
print('=~=~' * 20)
print(f'You entered the values {sorted(numbers)}')


