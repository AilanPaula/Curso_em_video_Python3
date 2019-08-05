def aumentar(p=0, tx=0, formato=False):
    res = p + (p * tx/100)
    return res if formato is False else moeda(res)


def diminuir(p=0, tx=0, formato=False):
    res = p - (p*tx/100)
    return res if formato is False else moeda(res)


def dobro(a=0, formato=False):
    res = a * 2
    return res if formato is False else moeda(res)


def metade(a=0, formato=False):
    res = a / 2
    return res if formato is False else moeda(res)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')
