'''
Crie um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
from datetime import date
n = int(input('Coloque 0 para calcular o ano atual ou digite o ano: '))
if n == 0:
    n = date.today().year
if ((n % 4 == 0) and (not(n % 100 == 0)) or (n % 400 == 0)):
    print('O ano {}, é bissexto '.format(n))
else:
    print('O ano {} não é bissexto '.format(n))