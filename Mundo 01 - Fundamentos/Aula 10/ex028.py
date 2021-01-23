"""
Escreva um programa que faça o computador "pensar" em um
numero inteiro entre 0 a 5 e peça para o usuario tentar descobrir
qual foi o numero escolhido pelo computador. o programa devera
escrever na tela se o usuario venceu ou perdeu.
"""
from random import randint

pc = randint(0, 5) # faz o computador "PENSAR"
print('-=-' * 20)
print('VOu pensar em um numero entre 0 a 5. Tente adivinhar!')
print('-=-' * 20)

jogador = int(input('Em que numero eu pensei? ')) # Jogador tenta adivinhar
if jogador == pc:
    print('PARABENS!!! Voce conseguiu me vencer!')
else:
    print(f'GANHEI... Eu pensei no numero {pc} e não no {jogador} :)')
