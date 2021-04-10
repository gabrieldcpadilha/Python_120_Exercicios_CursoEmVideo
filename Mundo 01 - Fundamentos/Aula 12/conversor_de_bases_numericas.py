"""
Escreva um programa que leia um numero inteiro qualquer e peça
para o usuario escolher qual sera a base de conversão:
1 - para binario
2 - para octal
3 - hexadecimal
"""

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para Binario
[2] Converter para Octal
[3] Converter para Hexadecimal''')

opcao = int(input('Escolha sua opção: '))
if opcao == 1:
    print(f'{num} convertido para Binario é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para Binario é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para Binario é igual a {hex(num)[2:]}')
else:
    print('Opção Invalida!')
