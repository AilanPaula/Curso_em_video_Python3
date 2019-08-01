'''
Crie um programa para mostrar que tipo de triângulo será formado:
-> EQUILÁTERO: todos os lados iguais
-> ISÓSCELES: dois lados iguais, um diferente
-> ESCALENO: todos os lados diferentes
'''
ld1 = float(input('Valor lado 1: '))
ld2 = float(input('Valor lado 2: '))
ld3 = float(input('Valor lado3: '))

if ld1 == ld2 and ld1 == ld3 and ld2 == ld3:
    print('Triangulo equilatero')
elif ld1 == ld2 or ld1 == ld3 or ld2 == ld1 or ld2 == ld3 or ld3 == ld1 or ld3 == ld2:
    print('Triangulo Isoceles')
else:
    print('Triangulo escaleno')