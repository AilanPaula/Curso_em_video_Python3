'''
Crie um programa que leia a quantidade  de KM percorridos por um carro alugado e a quantidade de dias que ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.
'''
d = int(input('Quantos dias alugados?: '))
km = float(input('Quantos km rodados?: '))
s = (km * 0.15) + (d * 60)
print('O total a pagar é de R$: {:.2f} '.format(s))