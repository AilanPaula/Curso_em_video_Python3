'''
Crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
-> Quantas vezes apareceu o valor 9.
-> Em que posição foi digitado o primeiro valor 3.
-> Quais foram os números pares.
'''
n = (int(input('Digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite mais um valor: ')),
     int(input('Digite último valor: ')))
print(f'Os valores digitados foram: {n}')
print(f'O valor 9 aparece {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 foi digitado na posição {n.index(3)+1}')
else:
    print('O valor 3 não aparece na lista. ')
print('Os números pares foram: ', end=' ')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')