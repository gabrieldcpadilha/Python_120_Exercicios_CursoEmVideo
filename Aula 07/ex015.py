"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
km = float(input('Digite quantos Km percorridos: '))
dias = int(input('Digite a quantidade de dias alugado: '))
pagamento = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${pagamento:.2f}')
