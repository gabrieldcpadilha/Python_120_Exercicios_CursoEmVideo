"""
Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual será o valor a ser sacada (numero inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

EXEMPLO:
====================================
            BANCO CEV
====================================
Que valor você quer sacar? R$ 1234
Total de 24 cédulas de R$50
Total de 1 cédulas de R$20
Total de 1 cédulas de R$10
Total de 4 cédulas de R$1
====================================
Volte sempre ao BANCO CEV! Tenha um bom dia!
"""
print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)
valor = int(input('Que valor você quer sacar? R$'))
montante = valor
cedula = 50
total_de_cedula = 0
while True:
    if montante >= cedula:
        montante -= cedula
        total_de_cedula +=1
    else:
        if total_de_cedula > 0:
            print(f'Total de {total_de_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_de_cedula = 0
        if montante == 0:
            break

print('='*40)
print('Volte sempre ao Banco CEV! Tenha um bom dia!')
