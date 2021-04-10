"""
Faça um programa que leia um numero de 0 a 9999 e mostre na tela
cada um dos digitos separados.

EX:
Digite um numero: 1834
Unidade: 4    Dezena: 3    Centena: 8    Milhar: 1
"""
numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Analisando o numero {numero}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
