"""
Elaboreum programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

- a vista dinheiro/cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra sera parcelada em 2x de R${parcela}')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_de_parcelas = int(input('Quantas parcelas deseja? '))
    parcela = total / total_de_parcelas
    print(f'Sua compra sera parcelada em {total_de_parcelas}x de R${parcela} com juros.')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
