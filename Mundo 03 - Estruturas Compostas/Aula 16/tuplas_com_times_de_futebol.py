"""
Crie um tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time do Corinthians.

EXEMPLO:

"""

times = ('Flamengo', 'Internacional', 'Atlético-MG',
         'São Paulo', 'Fluminense', 'Grêmio',
         'Palmeiras', 'Santos', 'Athletico-PR',
         'Bragantino', 'Ceará', 'Corinthians',
         'Atlético Goianiense', 'Bahia', 'Sport',
         'Fortaleza EC', 'Vasco da Gama', 'Goiás',
         'Coritiba', 'Botafogo')
#print(f'Lista de times: {times}')

print(f'Lista de times: {times[:5]}')
print(f'Os 4 últimos colocados da tabela: {times[-4:]}')
print(f'Times ordenados alfabéticamente: {sorted(times)}')
print(f'Corinthians está na {times.index("Corinthians")+1}ª posição da tabela.')
