"""
Escreva um programa que leia um numero n inteiro qualquer e
mostre na tela os n primeiros elementos de uma sequencia de
Fibonacci.

EX:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

t1 = 0
t2 = 1
contador = 3

n = int(input('Quantos termos quer mostrar? '))
print(f'{t1} -> {t2}', end='')
while contador <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    contador +=1
print(' -> FIM')
