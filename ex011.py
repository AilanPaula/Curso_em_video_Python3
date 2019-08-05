'''
Crie um programa que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto. 
'''
n = float(input('Qual o preço do produto?: '))
p = n-(n*5/100)
print('O produto que custava {}, na promoção com desconto de 5% vai custar {:.2f}. '.format(n,p))
