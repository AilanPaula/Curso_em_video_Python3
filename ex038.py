'''
Crie um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
->1 para binário
->2 para octal
->3 para hexadecimal.
'''
num = int(input('Digite um número inteiro: '))
op = int(input('Escolha uma das opções: \n[1] - Binário \n[2] - Octal \n[3] - Hexadecimal \n'))
if op == 1:
    print('O número {} em binário é: {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} em octal é: {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} em hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Digite um número válido.')