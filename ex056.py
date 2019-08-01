'''
Crie um programa que pergunte para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
soma = p
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(soma), end=' ')
        soma = soma + r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar?: '))
print('FIM')
