"""
Faça um programa que calcule a soma
entre todos os numeros impares que sao
multiplos de tres e que se encontram no
intervalo de 1 até 500.
"""

soma = 0
cont = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é: {soma}')
