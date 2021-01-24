"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um numero entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessarios para vencer.
"""

from random import randint

pc = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será que voce consegue adivinhar qual foi?')
acertou = False
errou = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    errou += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente denovo.')
        elif jogador > pc:
            print('Menos... Tente denovo.')
print('Parabéns, ACERTOU!!!')
print(f'Você acertou o numero {pc} em {errou} palpites')
