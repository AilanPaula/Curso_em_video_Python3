'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
-> Quantas pessoas tem mais de 18 anos.
-> Quantos homens foram cadastrados.
-> Quantas mulheres tem menos de 20 anos.
'''
print('-' * 30)
print('Cadastre uma pessoa')
print('-' * 30)
total_pessoas = homens = mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        total_pessoas += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulher += 1
    tipo = ' '
    while tipo not in 'SN':
        tipo = str(input('Quer continuar?: [S/N]')).upper().strip()[0]
    if tipo == 'N':
        break
print(f'Total de pessoa com mais de 18 anos: {total_pessoas}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')
