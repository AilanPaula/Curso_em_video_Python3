'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
valor = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valor[-1]:
        valor.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valor):
            if n <= valor[pos]:
                valor.insert(pos,n)
                print(f'Adicionado na posição {pos+1} da lista.')
                break
            pos +=1
print(f'Os valores digitados foram {valor}')
