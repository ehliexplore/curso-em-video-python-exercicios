import moeda

n = float(input('Digite um valor em R$: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(n, 10, True)}')
print(f'Diminuindo 10% temos {moeda.diminuir(n, 10, True)}')





