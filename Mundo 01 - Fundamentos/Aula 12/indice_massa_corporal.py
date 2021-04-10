"""
Desenvolva uma logica que leia o peso e a altura de uma pessoa.
Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade morbida
"""

altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))

imc = peso / (altura ** 2)
print(f'O IMC é de: {imc}')

if imc < 18.5:
    print('ABAIXO DO PESO normal.')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL.')
elif imc > 25 and imc <= 30:
    print('SOBREPESO.')
elif imc > 30 and imc >= 40:
    print('OBESIDADE.')
else:
    print('OBESIDADE MORBIDA.')