'''
Crie um programa que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento.
'''
n = float(input('Qual é o salário do funcionário?: '))
s = n + (n*15/100)
print('Um funcionário que ganhava {}, com 15% de aumento, passa a ganhar {:.2f}.'.format(n,s))