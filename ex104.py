def integer(string):
    ok = False
    v = 0
    while True:
        a = str(input(string))
        if a.isnumeric():
            v = int(a)
            ok = True
        else:
            print('ERROR. Insert a valid integer number.')
        if ok:
            break
    return v


a = integer('Enter a number: ')
print(f'You entered the number {a}')


