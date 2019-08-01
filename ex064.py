'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
-> Qual é o total gasto na compra.
-> Quantos produtos custam mais de R$1000.
-> Qual é o nome do produto mais barato.
'''
print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
total = produto = menor = cont = 0
barato = ' '
while True:
    nome_produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    resp = ' '
    total += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome_produto
    if preco >= 1000:
        produto +=1
    while resp not in 'SN':
        resp = str(input('Quer continuar?: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de: R$ {total:.2f}')
print(f'Temos {produto} produtos  custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R$: {menor:.2f}')
