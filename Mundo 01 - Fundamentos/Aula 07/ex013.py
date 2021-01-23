"""
Faça um programa que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.
"""

salario = float(input('Informe seu salário: R$'))
novo_salario = salario + (salario * 15 / 100)

print(f'O funcionário ganhava R${salario}')
print(f'Com 15% de aumento, seu novo salário passa a ser: R${novo_salario:.2f}')
