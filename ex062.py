'''
Crie um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
print('-' * 30)
print('Vamos jogar Par ou Impar')
print('-' * 30)
cont = 0
while True:
    n = int(input('Digite um valor: '))
    resp = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    computador = randint(0,10)
    soma = n + computador

    if soma % 2 == 0:
        print(f'Você jogou {n} e o computador {computador}. Total de {soma} deu PAR')
        if resp == 'P':
            print('Você venceu. Vamos jogar novamente')
            cont +=1
        else:
            break
    else:
        print(f'Você jogou {n} e o computador {computador}. Total de {soma} deu IMPAR')
        if resp == 'I':
            print('Você venceu. Vamos jogar novamente')
            cont +=1
        else:
            break
print('Você perdeu')
print(f'Game Over. Você venceu {cont} vezes')