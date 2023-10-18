# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Que ano você quer analisar? '))
a1 = ano % 4
if a1 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'{ano} é Bissexto.')
else:
  print(f'{ano} não é Bissexto.')