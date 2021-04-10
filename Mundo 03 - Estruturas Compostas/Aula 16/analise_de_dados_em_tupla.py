"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.

EXEMPLO 1:
Digite um número: 2
Digite outro número: 4
Digite mais um número: 6
Digite o último número: 8
Você digitou os valores (2, 4, 6, 8)
O valor 9 apareceu 0 vezes
O valor 3 NÃO FOI DIGITADO EM NENHUMA posição.
Os valores pares digitados foram 2 4 6 8

EXEMPLO 2:
Digite um número: 5
Digite outro número: 9
Digite mais um número: 2
Digite o último número: 3
Você digitou os valores (5, 9, 2, 3)
O valor 9 apareceu 1 vezes
O valor 3 APARECEU NA 4ª posição.
Os valores pares digitados foram 2
"""
num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))

print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 APARECEU na {num.index(3)+1} posição')
else:
    print(f'O valor 3 NÃO APARECEU EM NENHUMA posição')

print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
