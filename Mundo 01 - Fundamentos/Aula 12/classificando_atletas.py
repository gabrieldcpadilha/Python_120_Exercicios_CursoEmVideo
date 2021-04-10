"""
A Confederação Nacional de Notacao precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria de
acordo com a idade:
- até 9 anos: Mirim
- até 14 anos: Infantil
- Até 19 anos: Junior
- até 25 anos: Senior
- Acima: Master
"""

from datetime import date
atual = date.today().year

nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento

print(f'O Attleta tem {idade} anos')

if idade <= 9:
    print('Classificação: MIRIM.')
elif idade <= 14:
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print('Classificação: JUNIOR.')
elif idade <= 25:
    print('Classificação: SENIOR.')
else:
    print('Classificação: MASTER')