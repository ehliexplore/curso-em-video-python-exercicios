dados = dict()
gols_lista = []
jogadores = []
quant = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Atleta: '))
    quant = int(input('Quantidade de partidas jogadas: '))
    for c in range(0, quant):
        gols_lista.append(int(input(f'Quantidade de gols na partida {c+1}: ')))
    dados['gols'] = gols_lista[:]
    dados['total'] = sum(gols_lista)
    gols_lista.clear()
    jogadores.append(dados.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if continuar == 'N':
        break
print(jogadores)
print('=*~#' * 20)
print('COD ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 45)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('========================================')
while True:
    menu = int(input('Qual jogar você quer ver? [sair: 999]: '))
    if menu == 999:
        break
    if menu < len(jogadores):
        print(f'Mostrando dados do jogador {jogadores[menu]["nome"]}')
        for k, v in jogadores[menu].items():
            print(f'{str(k):<15} -> {str(v):^5}')
        for i, g in enumerate(jogadores[menu]["gols"]):
            print(f'No jogo {i} ele fez {g} gols.')
    else:
        print('Escolha um número de jogador válido.')






