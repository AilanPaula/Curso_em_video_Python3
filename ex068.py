'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint
tp = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados são: {tp}')
print(f'O maior valor sorteado foi: {max(tp)}')
print(f'O menor valor sorteado foi: {min(tp)}')