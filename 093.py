jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome: ')).capitalize()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1} fez {v} gols.')
print(f'Assim, um total de {jogador["total"]} gols.')
