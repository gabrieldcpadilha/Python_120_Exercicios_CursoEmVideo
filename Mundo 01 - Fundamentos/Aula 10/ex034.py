"""
Escreva um programa que pergunte o salario de um funcionario e
calcule o valor do seu aumento.
Para salarios superiores a R$1.250,00 calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Qual é o salario do funcionario: R$'))
if salario > 1250:
    novo = salario + (salario * 10 / 100)
    print(f'Seu salario era {salario} e agora passou a ser {novo}')
else:
    novo = salario + (salario * 15 / 100)
    print(f'Seu salario era {salario} e agora passou a ser {novo}')
