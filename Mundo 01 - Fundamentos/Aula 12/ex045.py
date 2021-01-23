"""
Crie um programa que faça o computador jogar Jokenpo com você.
"""
from random import randint
from time import sleep

mao = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Escolha sua mão? '))

print('''JO
...''')
sleep(1)
print('''KEN
...''')
sleep(1)
print('PO!')
sleep(1)
print('-=' * 15)

print(f'O COMPUTADOR jogou {mao[pc]}')
print(f'Você jogou {mao[jogador]}')
print('-=' * 15)

if pc == 0: # PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada invalida')

elif pc == 1: # PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada invalida')

elif pc == 2: # TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')
