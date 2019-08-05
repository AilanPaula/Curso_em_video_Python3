'''
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado e mostre no final:
-> A soma de todos os valores pares digitados.
-> A soma dos valores da terceira coluna.
-> O maior valor da segunda linha.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = scol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]'))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
for l in range(0, 3):
    scol += matriz[l][2]
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'A soma dos valores pares é: {soma}')
print(f'A soma da tarceira coluna é: {scol}')
print(f'O maior valor da segunda coluna é: {maior}')
