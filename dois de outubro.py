candidato = dict()
grupo = []

while True:
    candidato.clear()
    candidato['nome'] = str(input('Nome do candidato: '))
    candidato['número'] = int(input('Número: '))
    while True:
        candidato['cargo'] = str(input('Cargo disputado [P/G/DF/DE/S]: ')).upper()
        if candidato['cargo'] not in 'PGDFDES':
            print('Erro! Digite um cargo válido.')
        else:
            break
    grupo.append(candidato.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro. Digite S ou N.')
    if continuar == 'N':
        break

print(grupo)
print('x' * 20)


print('Os candidatos a PRESIDENTE são: ')
for c in grupo:
    if c['cargo'] == 'P':
        print(c['nome'])
print('Os candidatos a DEPUTADO FEDERAL são: ')
for c in grupo:
    if c['cargo'] == 'DF':
        print(c['nome'])


