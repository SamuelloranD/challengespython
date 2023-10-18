# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime
atual = datetime.date.today().year
maior = 0
menor = 0
for pessoas in range(1, 8):
  nascimento = int(input('Digite em que ano você nasceu: '))
  idade = atual - nascimento
  if idade >= 18:
    maior += 1
  else:
    menor += 1
print(f'Dessas pessoas, {maior} são maiores de idade e {menor} são menores de idade')