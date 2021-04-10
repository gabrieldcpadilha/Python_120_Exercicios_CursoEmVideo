"""
Crie um programa que leia o nome completo de uma pessoa e mostra:

* O nome com todas as letras maiusculas.
* O nome com todas as letras minusculas.
* Quantas letras ao total (sem considerar espaços).
* Quantas letras tem o primeiro nome.
"""

nome = input('Digite seu nome completo: ').strip()

print(f'Seu nome em maiusculo é {nome.upper()}')
print(f'Seu nome em minusculo é {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()

print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
