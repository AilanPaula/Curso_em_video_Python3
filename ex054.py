'''from math import factorial

n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)

print('O fatorial de {} é {}. '.format(n, f))'''

n = int(input('Digite um número para calcular o seu fatorial: '))
cont = n
f = 1
while cont != 0:

    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f = f * cont
    cont = cont - 1
print(f)
