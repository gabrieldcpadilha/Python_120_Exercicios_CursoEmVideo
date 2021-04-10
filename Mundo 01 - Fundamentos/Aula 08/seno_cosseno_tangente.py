"""
Faça um programa que leia um angulo qualquer e mostre na tela o valor de:
seno, cosseno e tangente deste angulo.
"""
from math import cos, sin, tan, radians

angulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O angulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O angulo de {angulo} tem o TANGENTE de {tangente:.2f}')
