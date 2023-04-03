jogador = dict()
gols = []
jogador['Nome'] = str(input('Atleta: '))
quant = int(input('Quantas partidas ele jogou? '))
for c in range(0, quant):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['Gols'] = gols
jogador['Total'] = sum(gols)
print('=~-' * 20)
print(jogador)
print('=~-' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('=~-' * 20)
print(f'O jogador {jogador["Nome"]} jogou {quant} partidas.')
for i, v in enumerate(gols):
    print(f'Na partida {i+1} ele fez {v} gols')
print(f'Foi um total de {jogador["Total"]} gols.')




