"""
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for NEGATIVO.
EXEMPLO:
---------------------------------------
Quer ver a tabuada de qual valor? 2
---------------------------------------
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
---------------------------------------
Quer ver a tabuada de qual valor? -1
---------------------------------------
PROGRAMA TABUADA ENCERRADO. Volte sempre!
"""

while True:
    print('-' * 40)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if num < 0:
        break
    else:
        for c in range(1, 11):
            resultado = num * c
            print(f'{num} x {c} = {resultado}')

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
