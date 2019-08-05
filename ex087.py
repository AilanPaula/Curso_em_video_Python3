'''
um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def area(l, c):
    calc = l * c
    print(f'A area de um terreno {l} x {c} é de: {calc}')

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)