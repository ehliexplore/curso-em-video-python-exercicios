numbers = list()
while True:
    numbers.append(int(input('Enter a value: ')))
    choice = str(input('Want to continue [Y/N]: ')).upper().strip()[0]
    if choice == 'N':
        break
print(f'You added {len(numbers)} numbers to the list.')
numbers_show = sorted(numbers, reverse=True)
print('The numbers in descending order are: ', end=' ')
print(numbers_show)
if 5 in numbers:
    print('The number 5 is on the list at position', end=' ')
    for i, v in enumerate(numbers):
        if v == 5:
            print(f'{i}.')
else:
    print('The number 5 is not on the list.')


