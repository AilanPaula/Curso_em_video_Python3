'''
Crie um programa que leia duas notas e calcule a sua média.
'''
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = ((n1+n2)/2)
print('A média entre {} e {} é igual a {:.1f} '.format(n1, n2, m))