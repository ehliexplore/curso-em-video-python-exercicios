def maior(* num):
    maior = 0
    cont = 0
    print('Analisando os números: ')
    for n in num:
        print(f'{n}', end=' ')
        if cont == 0:
            maior = n
        else:
            if maior < n:
                maior = n
        cont += 1
    print(f'Foram analisados {cont} números e o maior é {maior}', end=' ')



