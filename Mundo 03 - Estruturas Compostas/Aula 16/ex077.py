"""
Crie um programa que tenha uma tupla com várias palavras (Não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

Observação:
palavras = ('aprender', 'programar', 'linguagem', 'python')

EXEMPLO:
Na palavra APRENDER temos a e e
Na palavra PROGRAMAR temos o a a
Na palavra LINGUAGEM temos i u a e
Na palavra PYTHON temos o
"""

palavras = ('aprender', 'programar', 'linguagem', 'python')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
