pessoa = dict()
galera = []
soma = 0
contf = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    if pessoa['sexo'] == 'F':
        contf += 1
    pessoa['tamanho do pé'] = int(input('Tamanho do pé: '))
    galera.append(pessoa.copy())
    soma = soma + pessoa['idade']
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
             break
        print('ERRO! responda apenas com S ou N.')
    if resp == 'N':
        break
print('///' * 20)
print(galera)
print('///' * 20)
media = soma / len(galera)
print(f'No total temos {len(galera)} pessoas cadastradas.')
print(f'A soma das idades é {soma:5}')
print(f'A media das idades é {media:5.2f}')
if contf == 1 :
    print('Foi cadastrada uma pessoa do sexo feminino.')
    print('E ela é: ')
    for p in galera:
        if p['sexo'] == 'F':
            print(p['nome'])
elif contf > 0 and contf != 1:
    print(f'Foram cadastradas {contf} pessoas do sexo feminino.')
    print('E elas são: ')
    for p in galera:
        if p['sexo'] == 'F':
            print(p['nome'])
else:
    print(f'Nenhuma pessoa do sexo feminino foi cadastrada.')
if len(galera) > 1:
    print('As pessoas com idade maior que a média são: ')
    for c in galera:
        if c['idade'] > media:
            print(c['nome'])







