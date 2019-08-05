'''
um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def maior (* num):
    cont = maior = 0
    print('\nAnalisando os dados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor >= maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores')
    print(f'\nO maior valor é: {valor}')

maior(2, 4, 5, 1, 8)
maior(2,3)
maior(0)