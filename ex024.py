'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo")
'''
n = str(input('Qual o nome da cidade: ')).strip()
print(n[:5].upper() == 'SANTO')