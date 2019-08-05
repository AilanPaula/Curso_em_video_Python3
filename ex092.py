def fatorial(a, show = False):
    """
    -> Calcula o fatorial de um número qualquer digitado
    :param a: Valor referente ao calculo do fatorial
    :param show: Valor opcional para exibir todos os valores do calculo do fatorial
    :return: Retorna o valor final do calculo do fatorial do número digitado    
    """
    f = 1
    for c in range(a, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f*= c
    return f

print(fatorial(5, show=True))