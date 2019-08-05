'''
Crie um programa que gerencie o aproveitamento de vários jogadores de futebol.
'''
jogador = {}
time = list()
partida = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partida.clear()
    for c in range(1, tot + 1):
        partida.append(int(input(f'Quantos gols na partida {c} ? ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    resp = ' '
    while resp not in 'SN':
        resp = input('Você quer continuar? [S/N]').strip().upper()[0]
        if resp not in 'SN':
            print('ERRO! Digite um valor válido. S ou N')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for k in jogador.keys():
    print(f'{k:>15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para sair]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com o código {busca}')
    else:
        print(f' ---- LEVANTAMENTO DO JOGADOR ---- {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1}  fez  {g} gols.')