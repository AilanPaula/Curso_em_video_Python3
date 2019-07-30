'''
Crie um programa que leia quanto dinheiro uma pessoa possui na carteira e mostre quantos dólares ela pode comprar.
Considere U$$1,00 = R$3,27
'''
n = float(input('Quanto você tem na carteira? R$ '))
n2 = n/3.27
print('Você pode comprar {:.2f} dolares, com {} dinheiros.'.format(n2,n))