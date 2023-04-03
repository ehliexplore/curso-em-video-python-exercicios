teste = list()
galera = list()
teste.append('Luis')
teste.append(28)
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

