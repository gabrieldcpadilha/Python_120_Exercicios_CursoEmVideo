"""
Faça um programa que leia um
numero inteiro e diga se ele é
ou não um numero primo.
"""

n = int(input('Digite um número inteiro: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
