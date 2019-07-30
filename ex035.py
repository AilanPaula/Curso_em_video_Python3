'''
Crie um programa que leia 3 retas e mostre se o seguimento é um triângulo.
'''
a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro seguimento: '))

if a + b > c and a + c > b and b + c > a:
    print('O seguimento é um triangulo')
else:
    print('O seguimento não é um triangulo')