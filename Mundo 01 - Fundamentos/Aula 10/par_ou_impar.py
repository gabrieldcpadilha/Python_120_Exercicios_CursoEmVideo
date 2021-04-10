"""
Crie um programa que leia um numero inteiro
e mostre na tela se ele é PAR ou IMPAR.
"""

num = int(input('Digite um numero inteiro: '))
resultado = num % 2
if resultado == 0:
    print(f'O numero {num} é PAR.')
else:
    print(f'O numero {num} é IMPAR.')
