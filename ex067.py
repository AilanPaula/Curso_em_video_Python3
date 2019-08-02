'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
-> Os 5 primeiros times.
-> Os últimos 4 colocados.
-> Times em ordem alfabética.
-> Em que posição está o time Botafogo.
'''
times = ('Palmeiras', 'Santos','Flamengo','Atlético', 'Goias', 'Botafogo', 'Bahia', 'São Paulo', 'Corinthians')
print(f'Lista de times do Brasileirão: {times}', end='')
print(f'\nOs 5 primeiros são: {times[:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Botafogo está na posição: {times.index("Botafogo")+1}')