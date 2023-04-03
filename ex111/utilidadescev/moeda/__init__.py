def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)


def aumentar(n=0, taxa=0, formato=False):
    res = n + (n * taxa/100)
    return res if not formato else moeda(res)


def diminuir(n=0, taxa=0, formato=False):
    res = n - (n * taxa/100)
    return res if formato is False else moeda(res)


def moeda(n=0, price='R$'):
    f = (f'{price}{n:8>.2f}').replace('.',',')
    return f


def resumo(a, taxa=10, taxa2=5):
    print('=' * 30)
    print(f'RESUMO'.center(30))
    print('=' * 30)
    print(f'Metade do preço: \t{metade(a, True)}')
    print(f'Dobro do preço: \t{dobro(a, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(a, taxa, True)}')
    print(f'{taxa2}% de redução: \t\t{diminuir(a, taxa2, True)}')



