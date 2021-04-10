"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas ja sao maiores.
"""

from datetime import date
atual = date.today().year

maior = 0
menor = 0

for contador in range(0, 7):
    print('-=' * 20)
    nasc = int(input(f'Em que ano a {contador}* pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'''Maiores de idade: {maior}
Menores de idade: {menor}''')