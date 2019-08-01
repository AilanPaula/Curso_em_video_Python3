'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
cont = soma = media = maior = menor = 0
r = 'S'
while r in 'Ss':

    n = int(input('Digite um número: '))
    cont += 1
    soma = soma + n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N]:')).strip().lower()[0]
media = soma / cont
print('Você digitou {} números e média foi {}. '.format(cont, media))
print('O maior valor foi digitado foi {} e o menor foi {}. '.format(maior,menor))
