"""
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequêcia

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
Observação:
listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90)

EXEMPLO:
-------------------------------------
        LISTAGEM DE PREÇOS
-------------------------------------
Lápis.....................R$    1.75
Borracha..................R$    2.00
Caderno...................R$   15.90
Estojo....................R$   25.90
Transferidor..............R$    4.20
Compasso..................R$    9.99
Mochila...................R$  120.32
Canetas...................R$   22.30
Livro.....................R$   34.90
-------------------------------------
"""

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.90,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
