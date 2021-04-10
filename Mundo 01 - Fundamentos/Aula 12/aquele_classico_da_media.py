"""
Crie um programa que leia duas notas de um aluno e calcule sua media,
mostrando uma mensagem no final. de acordo com a media atingida:
- media abaixo de 5.0: Reprovado
- media entre 5.0 e 6.9: Recuperação
- media 7.0 ou superior: Aprovado
"""

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
print(f'A media do aluno foi: {media}')

if 5 <= media < 7:
    print('Aluno em RECUPERAÇÃO!')
elif media >= 7:
    print('Aluno APROVADO!')
else:
    print('Aluno REPROVADO!')
