'''
Crie um programa que leia o nome de quatro alunos e mostre a ordem sorteada.
'''
import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
names = [n1,n2,n3,n4]
random.shuffle(names)
print('A ordem de escolha é: {}' . format(names))