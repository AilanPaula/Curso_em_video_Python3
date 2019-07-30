'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
->O nome com todas as letras maiúsculas e minúsculas.
->Quantas letras ao todo(sem espaço)
->Quanatas letras tem o primeiro nome
'''
n = str(input('Digite seu nome completo: ')).strip() #strip retira espaço em branco no inicio e no final
print('Analisando seu nome...')
print('Seu nome em maiusculo é: {}'. format(n.upper()))
print('Seu nome em minusculo é: {}' . format(n.lower()))
print('Seu nome possui {} letras: '.format(len(n) - n.count(' ')))
''' len mostra o tamanho do string, count conta a quantidade de vezes que o mesmo elemento está contido na lista'''
#print('Seu primeiro nome possui {} letras: '.format(n.find(' ')))
separa = n.split()
print('Seu primeiro nome é {} e possui {} letras: '.format(separa[0], len(separa[0])))
