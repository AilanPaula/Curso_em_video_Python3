'''
Crie um programa que leia o comprimento do cateto oposto e cateto adjacente de um triângulo retângulo,
e calcule o valor da hipotenusa.
'''
from math import hypot

catadj = float(input('Digite o valor do cateto adjacente: '))
catopos = float(input('Digite o valor do cateto oposto: '))
# hip = math.sqrt((math.pow(catadj,2) + math.pow(catopos,2)))
hp = hypot(catopos,catadj)
print('O valor da hipotenusa é: {:.2f} '.format(hp))