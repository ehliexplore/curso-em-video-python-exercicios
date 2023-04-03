lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c}º valor: ')))
print(lista)

maior = max(lista)
menor = min(lista)
print(f'O maior valor é {maior} na posição', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}')
print()
print(f'O menor valor é {menor} na posição', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}')
