"""
Desenvolva um programa que pergunte a distancia de uma viajgem
em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
viagens de até 200Km e R$0,45 para viagens mais longas.
"""

distancia = float(input('Qual a distancia da sua viagem? '))
print(f'Você esta preste a comecar uma viagem de {distancia}Km')
if distancia <= 200:
    preco = distancia * 0.50
    print(f'O preço da sua viagem sera de R${preco}')
else:
    preco = distancia * 0.45
    print(f'O preço da sua viagem sera de R${preco}')
