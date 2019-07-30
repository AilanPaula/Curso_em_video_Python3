'''
Crie um programa que leia um ângulo qualquer e  mostre na tela o valor do seno, cosseno e tangente.
'''
import math

ang = float(input('Digite o angulo que deseja: '))
print('O angulo de {:.1f} tem SENO  de {:.1f}: '.format(ang, math.sin(math.radians(ang))))
print('O angulo de {:.1f} tem o COSSENO de {:.1f}: '.format(ang,math.cos(math.radians(ang))))
print(('O angulo de {:.1f} tem a TANGENTE de {:.1f}: '.format(ang,math.tan(math.radians(ang)))))