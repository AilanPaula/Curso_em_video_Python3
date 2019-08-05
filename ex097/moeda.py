def aumentar(p=0, tx=0):
    res = p + (p * tx/100)
    return res


def diminuir(p=0, tx=0):
    res = p - (p*tx/100)
    return res


def dobro(a=0):
    res = a * 2
    return res


def metade(a=0):
    res = a / 2
    return res


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')
