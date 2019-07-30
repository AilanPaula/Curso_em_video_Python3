'''
Crie um programa que leia o nome de um pessoa e mostre se ela possui ou não "Silva" no nome.
'''
nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome tem Silva?: {}'.format('silva' in nome.lower()))