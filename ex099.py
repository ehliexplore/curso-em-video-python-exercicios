def bigger(*n):
    print('Analyzing the values: ', end=' ')
    cont = big = 0
    for v in n:
        print(f'{v}', end=' ')
        if cont == 0:
            big = v
        else:
            if v > big:
                big = v
        cont += 1
    print(f'\n{cont} values were analyzed.')
    print(f'\nThe biggest value is {big}')
    cont = 0
    for s in n:
        if cont == 0:
            small = s
        else:
            if s < small:
                small = s
        cont += 1
    print(f'The smallest value is {small}')

bigger(-1, 57, 3, 4, 0)
