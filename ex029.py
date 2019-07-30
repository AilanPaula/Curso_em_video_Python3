'''
Crie um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
multado. A multa vai custar R$7,00 por cada KM acima do limite.
'''
v = float(input('Qual é a velocidade do carro?: '))
if v > 80.0:

    r = (v - 80.0) * 7.0
    print('Você passou com a velocidade de {}, e foi multado em {}: '.format(v, r))
else:
    print('Você passou com a velocidade {} e está dentro do limite permitido. '.format(v))