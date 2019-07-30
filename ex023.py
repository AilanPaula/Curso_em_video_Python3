'''
Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex: Digite um número: 1834
Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1
'''
n = int(input('Informe um número: '))
'''num = str(n)
print('Analisando o número {}: '.format(n))
print('Unidade {}: '.format(n[3]))
print('Dezena {}: '.format(n[2]))
print('Centena {}: '.format(n[1]))
print('Milhar {}: '.format(n[0]))'''

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analisando o número {}: '.format(n))
print('Unidade {}: '.format(u))
print('Dezena {}: '.format(d))
print('Centena {}: '.format(c))
print('Milhar {}: '.format(m))