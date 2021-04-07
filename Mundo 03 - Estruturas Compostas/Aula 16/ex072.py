"""
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.

EXEMPLO:
Digite um número entre 0 e 20: 90
Tente novamente. Digite um número entre 0 e 20: 13
Você digitou o número treze
"""

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    numero = int(input('Digite um número entre 0 e 20:  '))
    # Validando se o usuario digitou os numeros entre 0 e 20
    if numero < 0 or numero > 20:
        print('Tente novamente...', end='')
    else:
        print(f'Você digitou o número {extenso[numero]}')

        # Validando se o usuário quer continuar ou não
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta == 'N':
            break

print('{:-^40}'.format('FIM DO PROGRAMA'))
