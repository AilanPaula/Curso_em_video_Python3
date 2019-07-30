'''
Crie um programa que leia o salário de um funcionário e calcule o valor do seu aumento.
Para salários acima de R$1.250,00, calcule o aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Digite o salario R$: '))
if salario > 1250:
    print('O seu novo salario é: {:.2f}'.format(salario * 1.10))
else:
    print('O seu novo salario é: {:.2f}'.format(salario * 1.15))