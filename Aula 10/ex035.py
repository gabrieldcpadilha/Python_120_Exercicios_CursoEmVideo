"""
Desenvolva um programa que leia o comprimento
de tre retas e diga ao usuario se elas podem ou
nao formar um triangulo.
"""

reta1 = float(input('Informe o primeiro comprimento: '))
reta2 = float(input('Informe o segundo comprimento: '))
reta3 = float(input('Informe o terceiro comprimento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os comprimentos acima PODEM FORMAR um triangulo.')
else:
    print('Os comprimentos acima NÃO PODEM FORMAR um triangulo.')