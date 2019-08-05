'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
-> Quantas pessoas foram cadastradas
-> A média de idade
-> Uma lista com as mulheres
-> Uma lista de pessoas com idade acima da média
'''
dados = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = (str(input('Nome: ')))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
        if sexo not in 'MF':
            print('ERRO! Digite um valor válido. M ou F')
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    dados.append(pessoa.copy())
    resp = ' '
    while resp not in 'SN':
        resp = input('Você quer continuar? [S/N]').strip().upper()[0]
        if resp not in 'SN':
            print('ERRO! Digite um valor válido. S ou N')
    if resp == 'N':
        break
media = soma / len(dados)
print('-='*30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
print(f'B) A média de idade é de: {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in dados:
    if p['idade'] >= media:
        print(f'{p["nome"]}: {p["idade"]} anos, ', end='')
print()
