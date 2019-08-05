'''
um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
from random import randint
from time import sleep
lista = list()
def sorteia(lst):
    print('Os valores sorteados são: ', end='')
    print()
    for c in range(0, 5):
        n = randint(1, 10)
        lst.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)

def somapar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'\nSomando os valores pares da lista {lst} é: {soma}', end='')

sorteia(lista)
somapar(lista)