'''
Crie um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-> Até 9 anos: MIRIM
-> Até 14 anos: INFANTIL
-> Até 19 anos: JÚNIOR
-> Até 25 anos: SÊNIOR
-> Acima de 25 anos: MASTER
'''
from datetime import date
nasc = int(input('Qual o ano de nascimento?: '))
data_atual = date.today().year
idade = data_atual - nasc

if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade > 19 and idade <= 25:
    print('Senior')
else:
    print('Master')