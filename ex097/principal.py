'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), metade() e moeda().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
import moeda

num = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(num, 10))}')
