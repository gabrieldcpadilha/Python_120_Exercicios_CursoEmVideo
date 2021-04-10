"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer
mostrar 0 termos.
"""

p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = p1
contador = 1
mais_termos = 10
total = 0

while mais_termos != 0:
    total += mais_termos
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
