'''
Crie um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
-> Quantas pessoas foram cadastradas.
-> Uma listagem com as pessoas mais pesadas.
-> Uma listagem com as pessoas mais leves.
'''
dados = list()
aux = list()
maior = menor = 0.0
while True:
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = aux[1]
    else:
        if aux[1] > maior:
            maior = aux[1]

        if aux[1] < menor:
            menor = aux[1]
    dados.append(aux[:])
    aux.clear()

    resp = ' '
    while resp not in 'SN':
        resp = input('Você quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print(f'Ao todo você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {maior} kG. Peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor} KG')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')