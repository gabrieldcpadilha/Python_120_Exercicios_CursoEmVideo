"""
Faça um programa que leia um numero qualquer e mostre seu fatorial.

EX:
5! = 5x4x3x2x1 = 120
"""

num = int(input('Digite um numero para calcular seu fatorial: '))

contador = num
fatorial = 1

print(f'Calculando {num}! = ', end='')
for contador in range(num, 0, -1):
    print(f'{contador}',end='')
    print('x' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')
