"""
Crie um programa que leia varios numeros inteiros pelo teclado.
No final da execução, mostre a media entre todos os valores e qual
foi o maior e menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou nao continuar a digitar os valores.
"""

resposta = 'S'
soma = quantidade = media = maior = menor = 0

while resposta in 'Ss':
    num = int(input('Digite um numero inteiro: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? (S/N): ')).upper().strip()[0]
media = soma / quantidade
print(f'Voce digitou {quantidade} numeros e a media foi {media}')
print(f'O MAIOR numero digitado foi {maior}')
print(f'O MENOR numero digitado foi {menor}')
