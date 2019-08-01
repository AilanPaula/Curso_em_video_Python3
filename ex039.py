'''
Crie um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
-> O primeiro valor é maior
-> O segundo valor é maior
-> Não existe valor maior, os dois são iguais
'''
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num1 == num2:
    print('Os valores são iguais')
else:
    print('O segundo valor é maior')