"""
Faça um programa que leia um numero qualquer e mostre seu fatorial.

EX:
5! = 5x4x3x2x1 = 120
"""

from math import factorial

num = int(input('Informe um numero inteiro: '))
f = factorial(num)

print(f'O fatorial de {num}! = {factorial(num)}')
