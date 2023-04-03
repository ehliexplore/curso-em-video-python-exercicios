import moeda

n = float(input('Digite um valor em R$: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Diminuindo 10% temos {moeda.moeda(moeda.diminuir(n, 10))}')





