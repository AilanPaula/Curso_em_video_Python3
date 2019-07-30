'''
Crie um programa que faça o computador pensar em um número entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint

num = int(input('Em que número eu pensei?: '))
num2 = randint(0, 5)
if num == num2:
    print('Parabéns você me venceu!')
else:
    print('Ganhei, eu pensei no número {} e você no múmero {}. '.format(num2, num))