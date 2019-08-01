'''
Crie um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
n = int(input('Digite um número: '))
cont = 0
for c in range (1, n+1 ):
    print(c, end=' ')
    if n % c == 0:
        cont += 1
print('\nO número {} foi divisível {} vezes. '.format(n, cont))
if cont > 2:
    print('Ele não é primo')
else:
    print('Ele é primo')