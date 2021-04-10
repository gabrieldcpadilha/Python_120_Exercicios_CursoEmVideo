"""
Refaça o DESAFIO 009, mostrando a
tabuada de um numero que o usuário
escolher, só que agora utilizando um
laço for.
"""

n = int(input('Digite um número para ver sua tabuada: '))

print('-' * 15)
for c in range(1, 11):
    print(f'{c:2} x {n:2} = {n*c:2}')
print('-' * 15)
