words = ('programar', 'finalizar', 'amar', 'obedeço', 'obsecado')
for p in words:
    print(f'\nNa palavra {p} temos: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

