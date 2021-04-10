"""
Desenvolva um programa que leia o primeiro termo
e a razao de uma Progressão Aritmetica (PA),
no final, mostre os 10 primeiros termos dessa progressão.
"""

p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = p1 + (10 - 1) * razao
for c in range(p1, decimo + razao, razao):
    print(f'{c}', end='-> ')
print('FIM!')