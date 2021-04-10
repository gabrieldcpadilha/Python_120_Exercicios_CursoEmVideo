"""
Faça um programa que jogue PAR ou IMPAR com o computador.
O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

EXEMPLO:
    =-=-=-=-=-=-=-=-=-=-=-=-=-
    VAMOS JOGAR PAR OU IMPAR
    =-=-=-=-=-=-=-=-=-=-=-=-=-
    Diga um valor: 1
    Par ou Impar? [P/I]: P
    --------------------------
    Você jogou 1 e o computador 5. Total de 6 DEU PAR
    --------------------------
    Você VENCEU!
    Vamos jogar novamente...
    =-=-=-=-=-=-=-=-=-=-=-=-=-
    Diga um valor: 2
    Par ou Impar? [P/I]: P
    --------------------------
    Você jogou 2 e o computador 7. Total de 9 DEU IMPAR
    --------------------------
    Você PERDEU!
    =-=-=-=-=-=-=-=-=-=-=-=-=-
    GAME OVER! Você venceu 1 vezes.
"""

from random import randint

vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 10)
    resultado = jogador + pc
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? (P/I): ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}. Total de {resultado}', end=' ')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU IMPAR.')
    if escolha == 'P':
        if resultado % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if resultado % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar denovo...')
print(f'GAME OVER! Você venceu {vitoria} vezes.')
