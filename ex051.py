'''
Crie um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Informe é o seu sexo [ M/F]?: ')).upper().strip()[0]

while sexo not in 'MFmf':
    sexo = str(input('Dados inválidos. Digite um sexo válido')).strip().upper()[0]
print('Sexo {} valido. '.format(sexo))