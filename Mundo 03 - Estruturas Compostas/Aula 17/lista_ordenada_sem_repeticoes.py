lista = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Número adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Número adicionado na posição {pos} da lista...')
                break
            pos += 1
print('~~'*30)
print(f'Os valores digitados em ordem foram: {lista}')
