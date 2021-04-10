"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razao de uma PA.
Mostrando os 10 primeiros termos da progressao usando a estrutura while.

p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = p1 + (10 - 1) * razao
for c in range(p1, decimo + razao, razao):
    print(f'{c}', end='-> ')
print('FIM!')
"""

p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = p1
contador = 1

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador +=1
print('FIM')