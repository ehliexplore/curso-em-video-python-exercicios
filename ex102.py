def fatorial(a, show=False):
    """
    Calcula o fatorial.
    :param a: Número a ser calculado.
    :param show: Se show=True, mostra o cálculo do fatorial.
    :return: O valor do fatorial de um número a.
    """
    cont = 1
    for n in range(a, 0, -1):
        if show:
            if n > 1:
                print(f'{n} x ', end='')
            else:
                print(f'{n} = ', end='')
        cont *= n
    return f'{cont}'


print(fatorial(5, show=True))
help(fatorial)



