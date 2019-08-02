'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
-> Quantos números foram digitados.
-> A lista de valores, ordenada de forma decrescente.
-> Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = input('Você quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print(f'Você digitou {len(lista)} elementos. ')
print(f'Os valores em ordem descrente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor não 5 não faz parte da lista')