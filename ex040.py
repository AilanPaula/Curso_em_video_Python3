'''
Crie um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Oprograma também deverá mostrar o tempo que falta ou que já passou do prazo.
'''
from datetime import date

ano = int(input('Qual o ano de nascimento?: '))
data_atual = date.today().year
idade = data_atual - ano

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, data_atual))

if idade == 18:
    print('Você tem que alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    dt = data_atual + saldo
    print('Ainda faltam {} para o seu alistamento. '.format(saldo))
    print('O seu alistamento irá ocorrer em: {}'.format(dt))
elif idade > 18:
    saldo = idade - 18
    dt = data_atual - saldo
    print('Você deveria ter se alistado há {} anos. '.format(saldo))
    print('Seu alistamento foi no ano de: {}'.format(dt))