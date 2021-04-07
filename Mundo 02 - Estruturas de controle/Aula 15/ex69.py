"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.

EXEMPLO:
----------------------------
    CADASTRE UMA PESSOA
----------------------------
Idade: 33
Sexo: [M/F] M
----------------------------
Quer continuar? [S/N] S
----------------------------
    CADASTRE UMA PESSOA
----------------------------
Idade: 19
Sexo: [M/F] G
Sexo: [M/F] X
Sexo: [M/F] F
----------------------------
Quer continuar? [S/N] 25
Quer continuar? [S/N] N
----------------------------
====== FIM DO PROGRAMA ======
Total de pessoas com mais de 18 anos: 2
No total temos 1 homens cadastrados
E temos 1 mulheres com menos de 20 anos
"""
idade = maior_18_anos = total_de_homens = total_de_mulheres = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    if idade <= 0:
        print('Informe uma idade MAIOR que 0')
    else:
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if idade >= 18:
            maior_18_anos += 1
        if sexo == 'M':
            total_de_homens += 1
        if idade < 20 and sexo == 'F':
            total_de_mulheres += 1

        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break

print(f'Total de pessoas com mais de 18 anos: {maior_18_anos}')
print(f'total temos {total_de_homens} homens cadastrados')
print(f'E temos {total_de_mulheres} mulheres com menos de 20 anos')
