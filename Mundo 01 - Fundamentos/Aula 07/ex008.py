"""
Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros.
"""

medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'Medida em centimetros: {cm}cm')
print(f'Medida em milimetros: {mm}cm')
# print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
