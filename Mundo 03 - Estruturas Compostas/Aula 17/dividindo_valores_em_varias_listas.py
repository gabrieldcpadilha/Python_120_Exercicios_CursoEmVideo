lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [s/n]'))
    if resposta in 'Nn':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print('='*30)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de impares é: {impar}')
