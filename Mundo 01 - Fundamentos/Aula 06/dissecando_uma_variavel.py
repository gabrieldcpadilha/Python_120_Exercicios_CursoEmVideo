"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possiveis sobre ele.
"""

entrada = input('Digite algo: ')
print('O tipo primitivo dessa entrada é: ', type(entrada))
print('Só tem espaços? ', entrada.isspace())
print('É um número? ', entrada.isnumeric())
print('É Alfabético? ', entrada.isalpha())
print('É Alfanumérico? ', entrada.isalnum())
print('Esta em Maiúscula? ', entrada.isupper())
print('Esta em Minúscula? ', entrada.islower())
print('Esta Capitalizada? ', entrada.istitle())
