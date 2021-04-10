"""
Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor
"""

valor1 = int(input('Informe o valor 1: '))
valor2 = int(input('Informe o valor 2: '))
valor3 = int(input('Informe o valor 3: '))

menor = valor1

if valor2 < valor1 and valor2 < valor3:
    menor = valor2
elif valor3 < valor1 and valor3 < valor2:
    menor = valor3

maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
elif valor3 > valor1 and valor3 > valor2:
    maior = valor3

print(f'O MENOR valor digitado foi {menor}')
print(f'O MAIOR valor digitado foi {maior}')
