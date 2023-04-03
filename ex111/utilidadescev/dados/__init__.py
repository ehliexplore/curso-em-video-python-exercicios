def leiaDinheiro(msg):
    valid = False
    while not valid:
        enter = str(input(msg)).replace(',', '.').strip()
        if enter.isalpha() or enter == '':
            print(f'{enter} é um preço inválido. Tente novamente.')
        else:
            valid = True
            return float(enter)


