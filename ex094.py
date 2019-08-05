'''
Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante 'a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
'''
def LeiaInt(resp):
    num = str(input(resp))
    if num.isnumeric():
        num = int(num)
        return num
    while not num.isnumeric():
        print('ERRO! Digite um número válido')
        num = str(input(resp))
    return num

'''def teste(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('ERRO! Digite um número válido')
        if ok:
            break
    return valor'''



#Programa principal
n = LeiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')