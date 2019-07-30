n = float(input('Qual o preço do produto?: '))
p = n-(n*5/100)
print('O produto que custava {}, promoção com desconto de 5% vai custar {:.2f}. '.format(n,p))