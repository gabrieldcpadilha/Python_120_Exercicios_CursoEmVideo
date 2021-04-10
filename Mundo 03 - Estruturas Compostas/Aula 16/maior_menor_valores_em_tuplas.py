"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

EXEMPLO:
Os valores sorteados foram: 5 7 5 4 6
O maior valor sorteado foi 7
O menor valor sorteado foi 4
"""
from random import randint

sorteio = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: {sorteio}')
print(f'O maior valor sorteado foi: {max(sorteio)}')
print(f'O menor valor sorteado foi: {min(sorteio)}')


"""EXERCICIO RESOLVIDO POR GUSTAVO GUANABARA:
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
"""
