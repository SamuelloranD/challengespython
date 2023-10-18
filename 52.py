# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

v = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1, 1):
  if num % c == 0:
    print('\033[32m', end='')
    v += 1
  else:
    print('\033[31m', end='')
  print(f'{c} ', end='')
print(f'\n\033[mO número digitado foi dividido {v} vezes.')
if v == 2:
  print('Portanto, ele é um número primo.')
else:
  print('Portanto, ele não é um número primo')