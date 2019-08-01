'''
Crie um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p1 + (10 -1) * r
for c in range (p1, d + r, r):
    print(c, end=' -> ')
print('ACABOU')