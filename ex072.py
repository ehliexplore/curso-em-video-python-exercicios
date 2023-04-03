numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
           'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
           'nineteen', 'twenty')

while True:
    choice = int(input('Choose a number between 0 and 20: '))
    if 0 <= choice <= 20:
        break
    print('Invalid number. Try again.')
print(f'You chose the number {numbers[choice]}.')





