def integer(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('Data entry was interrupted by the user.')
            return 0
        except (ValueError, TypeError):
            print('Invalid number. Insert an valid number.')
            continue
        else:
            return n



def floating(n2):
    while True:
        try:
            n2 = float(input('Enter an real number: '))
        except KeyboardInterrupt:
            print('User chose not to enter this number.')
            return 0
        except (TypeError, ValueError):
            print(f'Invalid real number. Insert an valid number.')
            continue
        else:
            return n2


user = integer('Enter an integer number: ')
print(f'The entered number was {user}')
user2 = floating('Enter an float number: ')
print(f'The entered floating number was {user2}')
