# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for p in range(1, 6):
  peso = float(input(f'Digite o peso da pessoa {p}: '))
  if p == 1:
    maior = p
    menor = p
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso
print(f'O maior peso informado foi {maior:.0f}Kg.')
print(f'O menor peso informado foi {menor}Kg.')
