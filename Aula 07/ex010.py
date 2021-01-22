"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
E mostre quantos Dolares ela pode comprar.

Considere US$1.00 = R$3.27
"""

real = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = real / 3.27

print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))
