"""
Escreva um programa para aprovar o emprestimo bancario para a
compra de uma casa. Pergunte o valor da casa, o salario do comprador
e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salario ou entao o
emprestimo sera negado.
"""

valor_casa = float(input('Qual o valor da casa? R$'))
anos = int(input('Quantos anos você deseja pagar? '))
salario_comprador = float(input('Qual o seu salario atual? R$'))

aprovado = salario_comprador * 30 / 100
mensalidade = valor_casa / (anos * 12)

print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos')
print(f'a prestação será de R${mensalidade:.2f}')

if mensalidade <= aprovado:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo NEGADO!')
