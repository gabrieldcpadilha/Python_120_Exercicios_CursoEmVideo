"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um tringulo retangulo.
Calcule e mostre o comprimento da hipotenusa.
"""

""" MODELO SEM IMPORT MATH
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')
"""

# MODELO COM IMPORT MATH
from math import hypot

co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')
