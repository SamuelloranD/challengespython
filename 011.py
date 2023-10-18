# Faça um programa que pergunte a altura e a largura de uma parede em metros, calcule e área e a quantidade de tinta necessária para pintá-la, considerando que cada litro de tinta pinta uma área de 2m2.

l = int(input('Qual a largura da parede? '))
a = int(input('Qual a altura? '))
a2 = l*a
print(f'A área da sua parede é de {a2} metros quadrados. Assim, você irá precisar de {a2/2:.0f} litros de tinta para pintá-la por completo.')
