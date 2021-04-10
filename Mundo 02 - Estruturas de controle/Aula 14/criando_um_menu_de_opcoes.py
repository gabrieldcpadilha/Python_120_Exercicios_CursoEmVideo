"""
Crie um programa que leia dois valores e mostre um menu como a abaixo na tela:
Seu programa deverá realizar a operação solicitada em cada caso.

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa
"""

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('''   [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    opcao = int(input('Informe uma opção: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} = {soma}')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} = {multiplicacao}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando programa...')
        break
    else:
        print('Opção invalida. Tente novamente.')
    print('-=' * 15)
print('Fim do Programa.')
