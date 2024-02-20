# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

times = ('Botafogo', 'Bragantino', 'Flamengo', 'Palmeiras', 
        'Athletico - PR', 'Grêmio', 'Atlético - MG', 'Fortaleza', 
        'Fluminense', 'São Paulo', 'Cuiabá', 'Internacional', 'Bahia', 
        'Cruzeiro', 'Corinthians', 'Goiás', 'Vasco', 
        'Santos', 'Coritiba', 'América - MG')
print(f'Os cinco primeiros times são {times[0:5]}.')
print(f'Os últimos quatro colocados são {times[-4:]}.')
print(f'Times em ordem alfabética: {sorted(times)}.')
print(f'O Vasco está na posição: {times.index("Vasco")+1}.')

