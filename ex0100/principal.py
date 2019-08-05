'''
Crie uma função chamada leiaDinheiro() e faça a validação de dados para aceitar apenas valores que seja monetários.
'''
from ex0100.utilidadescev import moeda
from ex0100.utilidadescev import dado

num = dado.leiaDinheiro('Digite o preço: R$ ')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num, 10, True)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(num, 13, True)}')
