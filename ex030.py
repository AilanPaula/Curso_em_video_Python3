'''
Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar.
'''
n = int(input('Digite um número: '))

if (n % 2 == 0 ):
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))