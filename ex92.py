from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['nascimento'] = int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de trabalho (0 = nãotem): '))
if pessoa['CTPS'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
else:
    print('Não possui carteira de trabalho.')
for k, v in pessoa.items():
    print(f'{k} é {v}')

idade = datetime.now().year - pessoa['nascimento']
print(idade)
if pessoa['CTPS'] > 0:
    inicio = pessoa['contratação'] - pessoa['nascimento']
    print(inicio)
    print(f'Idade de aposentadoria: {inicio+35}')
  


