"""
Desenvolva um programa que leia seis
numeros inteiros e mostre a soma
apenas daqueles que forem pares. Se
o valor digitado for impar,
desconsidere-o.
"""

soma = 0
for c in range(1, 7):
    n = int(input(f'Digite o numero {c}: '))
    if n % 2 == 0:
        soma += n
print(f'A somatório dos numeros é: {soma}')
