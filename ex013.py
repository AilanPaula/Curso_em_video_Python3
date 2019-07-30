'''
Crie um programa que converta uma temperatura em Cº para Fº.
'''
c = float(input('Informe a temperatura em Cº: '))
f = (c * 9/5) + 32
print('A temperatura de {:.1f}Cº corresponde em Fahrenheit {:.1f}Fº. '.format(c,f))