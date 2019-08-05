'''
Crie um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
-> Quantidade de notas
-> A maior nota
-> A menor nota
-> A média da turma
-> A situação (opcional)
'''
def notas(*num, sit=False):
    d = dict()

    d['total'] = len(num)
    d['maior'] = max(num)
    d['menor'] = min(num)
    d['media'] = sum(num) / len(num)
    if sit:
        if d['media'] >=7:
            d['situação'] = 'BOA'
        elif d['media'] >=5:
            d['situação'] = 'RAZOAVEL'
        else:
            d['media'] = 'RUIM'
    return d


resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)