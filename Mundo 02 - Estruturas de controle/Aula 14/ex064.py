"""
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que
é a condição de parada. No final, mostre quantos numeros foram
digitados e qual foi a soma entre eles (desconsiderando o flag).

MINHA RESOLUÇÃO FOI:
num = soma = contador = 0

while num != 999:
    num = int(input('Digite um numero inteiro: '))
    if num != 999:
        soma += num
        contador += 1
    else:
        print(f'Finalizando o programa... Foram calculados {contador}')
print(f'E a soma total entre eles foi {soma}')
"""

# RESOLUÇÃO FEITA PELO GUSTAVO GUANABARA

num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))
