'''
um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep
def contador(a, b, c):
    print(f'Contagem de {a} até {b} de {c} em {c}', end='')
    print()
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont +=c
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= c
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez: ')
i = int(input('Ìnicio: '))
f = int(input('Final: '))
v = int(input('Intervalo: '))
contador(i, f, v)
