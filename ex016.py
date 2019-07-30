'''
Crie um programa que leia um número real e mostre na tela a sua porção inteira.
'''
import math

num =  float(input('Digite um número: '))
print('O número digitado foi {} , possui a porção inteira {}' .format(num, math.trunc(num)))