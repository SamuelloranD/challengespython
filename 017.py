# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
c1 = float(input('Digite o cateto adjascente '))
c2 = float(input('Digite o cateto oposto '))
h = math.hypot(c1, c2)
print(f'A hipotenusa desse triângulo mede {h:.0f}.')
