numbers = []
for c in range(0, 5):
    n = int(input('Enter a number: '))
    if c == 0 or n > numbers[-1]:
        numbers.append(n)
    else:
        position = 0
        while position < len(numbers):
            if n <= numbers[position]:
                numbers.insert(position, n)
                break
            position += 1
print(f'The entered numbers are {numbers}')

