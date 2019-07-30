n = float(input('Qual é o salário do funcionário?: '))
s = n + (n*15/100)
print('Um funcionário que ganhava {}, com 15% de aumento, passa a ganhar {:.2f}.'.format(n,s))