'''
Crie um progrma que leia o nome de quatro alunos e faça o sorteio de um deles na lista.
'''
import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
names = [n1,n2,n3,n4]
print('O aluno escolhido foi: {} '.format(random.choice(names)))