# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: EQUILÁTERO: todos os lados iguais; ISÓSCELES: dois lados iguais, um diferente; ESCALENO: todos os lados diferentes.

r1 = int(input('Digite o cumprimento da primeira reta: '))
r2 = int(input('Digite o cumprimento da segunda reta: '))
r3 = int(input('Digite o cumprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Essas retas formam um triângulo.')
  if r1 == r2 == r3:
    print('Esse triângulo é EQUILÁTERO.')
  elif r1 != r2 != r3 != r1:
    print('Esse triângulo é do tipo ESCALENO.')
  else:
    print('Esse triângulo é do tipo ISÓSCELES.')
else:
    print('Essas retas não podem formas um triângulo.')