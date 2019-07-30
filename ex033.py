'''
Crie um programa que leia 3 números e mostre qual é o maior e o menor.
'''
a = int(input('Primeiro numero: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
menor = a
maior = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print('O menor valor é {}, e o maior valor é {} '. format(menor, maior))