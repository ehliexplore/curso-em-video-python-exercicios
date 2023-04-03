from time import sleep

def guess():
    from random import randint
    number = randint(0, 10)
    guesser = int(input('Guess the number (1 to 10): '))
    while True:
        if guesser == number:
            break
        if guesser > number:
            print('the number is smaller.')
        if guesser < number:
            print('the number is bigger.')
        guesser = int(input('Try again. Guess the number: '))
    print('Congratulations!')
    print(f'{number} is the correct number!')


print('Hey, you!')
sleep(1)
while True:
    print('Do you wanna play a game?')
    answer = str(input('Answer [Y/N]: ')).upper().strip()[0]
    if answer == 'Y':
        guess()
        while True:
            answer2 = str(input('Wanna play again?  [Y/N]: ')).upper().strip()[0]
            if answer2 == 'Y':
                guess()
            if answer2 == 'N':
                break
    elif answer == 'N':
        print('Ok :[')
        break
    else:
        print('YES OR NO')
print('THE END.')





