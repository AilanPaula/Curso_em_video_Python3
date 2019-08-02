'''
Crie um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
n = []
maior = menor = 0
for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
      maior = menor = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
print(f'Você digitou os valores: {n}')
print(f'O maior valor é: {maior}, nas posições: ', end='')
for pos, i in enumerate(n):
    if i == maior:
        print(f'{pos}...', end='')
print(f'\nO menor valor é: {menor}, nas posições: ', end='')
for pos, i in enumerate(n):
    if i == menor:
        print(f'{pos}...', end='')
print()

