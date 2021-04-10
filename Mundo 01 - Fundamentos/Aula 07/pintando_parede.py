"""
Faça um programa que leia a largura e altura de uma parede em metros.
Calcule a sua area e a quantidade de tinta necessaria para pinta-la.
Sabendo que cada litro de tinta, pinta uma area de 2m quadrado.
"""
largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
tinta = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua area é de {area}m')
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta')