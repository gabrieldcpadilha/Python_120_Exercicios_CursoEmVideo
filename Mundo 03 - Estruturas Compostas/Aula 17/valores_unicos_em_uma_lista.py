valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor ADICIONADO com sucesso...')
    else:
        print('Valor DUPLICADO! Não foi adicionado...')

    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('=='*30)
print(f'Os valores digitados foram: {sorted(valores)}')
