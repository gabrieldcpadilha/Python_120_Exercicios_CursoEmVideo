"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao servico militar,
se é a hora de se alistar ou seja passou do tempo do alistamento.
Seu programa tambem devera mostrar o tempo que falta ou que
passou do prazo.
"""

from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE.')
elif idade > 18:
    prazo = idade - 18
    print(f'Voce ja deveria ter se alistado ha {prazo} anos')
    ano = atual - prazo
    print(f'Seu alistamento foi em {ano}')
else:
    prazo = 18 - idade
    print(f'Ainda faltam {prazo} anos para o alistamento')
    ano = atual + prazo
    print(f'Seu alistamento será em {ano}')
