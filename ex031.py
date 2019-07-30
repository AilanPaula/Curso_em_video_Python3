'''
Crie um programa que pergunte a distância de um viagem em KM. Calcule o preço da passagem,
cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas.
'''
d = float(input('Qual é a distancia da viagem?: '))

if d > 200:
    r = d * 0.45
    print('O preço da passagem é de: {}'. format(r))
else:
    r = d * 0.50
    print('O preço da passagem é de: {}'.format(r))