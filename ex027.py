'''
Crie um programa que leia o nome completo de um pessoa e mostre o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro: Ana
ùltimo: Souza
'''
nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('Seu primerio nome é: {}'.format(n[0]))
print('Seu ultimo nome é: {}'.format(n[len(n)-1]))
