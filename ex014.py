d = int(input('Quantos dias alugados?: '))
km = float(input('Quantos km rodados?: '))
s = (km * 0.15) + (d * 60)
print('O total a pagar é de R$: {:.2f} '.format(s))