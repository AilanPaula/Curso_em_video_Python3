'''
Crie um programa onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar em qual foi?')
acertou = False
ram = randint(0,10)
cont = 0

while not acertou:
    num = int(input('Qual o seu palpite?: '))
    cont +=1
    if num == ram:
        acertou = True
    else:
        if num < ram:
            print('Mais... Tente  mais uma vez.')
        elif num > ram:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. '.format(cont))
