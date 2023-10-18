# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

d = int(input('Qual a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {d:.1f} Km')
if d <=200:
  d1 = d * 0.50
  print(f'O preço da sua passagem será de R${d1:.2f}.')
else:
  d2 = d * 0.45
  print(f'O preço da sua passagem será de R${d2:.2f}.')