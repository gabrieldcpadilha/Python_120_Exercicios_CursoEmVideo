"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.

EXEMPLO:
---------------------------
    LOJA SUPER BARATÃO
---------------------------
Nome do Produto: Mouse
Preço: R$50
Quer continuar? [S/N] s
Nome do Produto: Caneta
Preço: R$3
Quer continuar? [S/N] s
Nome do Produto: Notebook
Preço: R$2800
Quer continuar? [S/N] n
------- FIM DO PROGRAMA -------
O total de compra foi: R$2853.00
Temos 1 produtos custando mais de R$1000.00
O produto mais barato foi Caneta que custa R$3.00
"""
a = b = c_preco = c_nome = contador = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    contador += 1
    a += preco
    if preco > 1000:
        b += 1

    if contador == 1 or preco < c_preco:
        c_preco = preco
        c_nome = produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA! '))
print(f'O total de compra foi: R${a:.2f}')
print(f'Temos {b} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {c_nome} que custa R${c_preco:.2f}')
