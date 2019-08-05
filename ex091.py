'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
from datetime import datetime
def voto(ano):
    idade = datetime.now().year - ano
    if idade >= 65 or 16 <= idade < 18:
        return f'Com {idade} anos: O voto é opcional'
    elif idade < 16:
        return f'Com {idade} anos: Não vota'
    else:
        return f'Com {idade} anos: O voto é obrigatório'


ano = int(input('Em que ano você nasceu?: '))
print(voto(ano))