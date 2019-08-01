'''
Crie um programa que mostre a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
'''
num = int(input('Digite um numero: '))

for c in range(1, 11):
    print('{} x {} = {} '. format(num, c, c* num))