'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0

while op !=5:
    print('\nMenu: \n[1]somar \n[2]multiplicar \n[3]maior \n[4]novos números \n[5]sair do programa \n')
    op = int(input('Qual a sua opções?: '))

    if op == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é: {}. '.format(n1, n2, soma))
    elif op == 2:
        produto = n1 * n2
        print('A multiplicação entre {} e {} é: {}. '.format(n1, n2, produto))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior  número entre {} e {} é: {}. '.format(n1, n2, maior))
    elif op == 4:
        print('Informe os número novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
        break
    else:
        print('Opção inválida. Digite um valor válido.')
print('Fim do programa. Volte sempre.')




