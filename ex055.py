'''
Crie um programa que leia o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0
soma = p

while cont < 10:

    print(soma, end=' ')
    soma = soma + r
    cont += 1
print('Fim')