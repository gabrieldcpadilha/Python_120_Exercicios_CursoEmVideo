"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
"""
soma = qtd_de_numeros = numero = 0

while True:
    numero = int(input('Digite um número (999 para sair do programa): '))
    if numero == 999:
        break
    soma += numero
    qtd_de_numeros += 1

print(f'Foram digitados {qtd_de_numeros} e a soma entre eles foi: {soma}')
