'''
Crie um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''
aluno = dict()

aluno['nome'] = str(input('Nome:'))
aluno['nota'] = float(input(f'Média de {aluno["nome"]}:'))

if aluno['nota'] <= 5:
    aluno['situação'] = 'Reprovado'
elif aluno['nota'] > 5 and aluno['nota'] <= 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')