def grades(*num, sit=False):
    """
    Função para analisar notas e mostrar situação de alunos.
    :param num: Notas (aceita várias)
    :param sit: Situação do aluno
    :return:Retorna dicionário mostrando informações de alunos
    """
    students = {}
    students['total'] = len(num)
    students['bigger'] = max(num)
    students['smallest'] = min(num)
    students['average'] = sum(num) / len(num)
    if sit:
        if students['average'] >= 7:
            print('Situation: GOOD')
        elif students['average'] >= 5:
            print('Situation: NOT TOO GOOD BUT OK')
        else:
            print('Situation: BAD')
    return students


a = grades(6, 10, 7, sit=True)
print(a)
help(grades)


