"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem
"SILVA" no nome.
"""
nome = input('Qual é o seu nome completo? ').strip()
print('Seu nome tem "SILVA"? {}'.format('SILVA' in nome.upper().split()))
