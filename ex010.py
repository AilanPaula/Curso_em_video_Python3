'''
Crie um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la.
Cada litro de tinto, pinta uma área de 2m².
'''
l = float(input('Largura da parede: '))
a = float(input('Altura da perede: '))
d = l*a
p = d/2
print('Sua parede tem a dimensão  de {}x{} e sua área é de {}m². '.format(l,a,d))
print('Para pintar a parede, você precisará de {} litros de tinta. '.format(p))
