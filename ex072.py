'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
valor = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('O valor digitado já existe.')
    resp = ' '
    while resp not in'SN':
        resp = input('Você quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break
valor.sort()
print(f'Você digitou os valores: {valor}')