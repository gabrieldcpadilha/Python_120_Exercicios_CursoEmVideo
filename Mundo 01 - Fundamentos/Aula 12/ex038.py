"""
Escreva um programa que leia dois numeros inteiros e compare-os
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é menor
- Não existe valor maior, os dois são iguais
"""

valor1 = int(input('Informe o valor 1: '))
valor2 = int(input('Informe o valor 2: '))

if valor1 > valor2:
    print('O PRIMEIRO valor é MAIOR!')
elif valor2 > valor1:
    print('O SEGUNDO valor é MAIOR')
else:
    print('Não existe valor maior, OS DOIS SÃO IGUAIS')
