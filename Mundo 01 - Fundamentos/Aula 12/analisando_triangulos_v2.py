"""
Refaça o DESAFIO 035 dos triangulos, acrescentando o recurso de
mostrar que tipo de triangulo sera formado:
- EQUILATERO: todos os lados iguais
- ISOSCELES: dois lados iguais
- ESCALENO: todos lados diferentes
"""

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM FORMAR um triangulo.')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos NÃO PODEM FORMAR um triangulo.')