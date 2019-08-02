'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
par = []
impar = []

while True:
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = input('Você quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de impares é: {impar}')