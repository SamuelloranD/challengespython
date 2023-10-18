# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Digite a velocidade do veículo: '))
if vel >80:
  v2 = (vel - 80) * 7
  print('Você ultrapassou o limite de velocidade.')
  print(f'Você foi multado em R${v2:.2f}.')
else:
  print('Você está dentro do limite de velocidade permitido.')
