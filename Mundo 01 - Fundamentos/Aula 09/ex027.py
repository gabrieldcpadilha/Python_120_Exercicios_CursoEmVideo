"""
Faça um programa que leia o nome completo de uma pessoa.
mostrando em seguida o primeiro e o ultimo nome separadamente.

EX: Ana Maria de Souza
Primeiro = Ana
Ultimo = Souza
"""
nome = input('Digite seu nome completo: ').strip()
lista = nome.split()
print('Prazer em te conhecer!')
print(f'Seu primeiro nome é {lista[0]}.')
# print(f'Seu ultimo nome é {lista[len(lista) - 1]}')
print(f'Seu ultimo nome é {lista[-1]}.')
