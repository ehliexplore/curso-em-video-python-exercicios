numbers = []
pairs = []
odds = []
while True:
    n = int(input('Insert a number: '))
    numbers.append(n)
    answer = str(input('Want to continue? [Y/N]: ')).strip().upper()[0]
    if answer == 'N':
        break
for i, v in enumerate(numbers):
    if v % 2 == 0:
        pairs.append(v)
    elif v % 2 != 0:
        odds.append(v)
print(numbers)
print(pairs)
print(odds)
