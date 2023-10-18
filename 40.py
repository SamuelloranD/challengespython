# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0: REPROVADO; Média entre 5.0 e 6.9: RECUPERAÇÃO; Média 7.0 ou superior: APROVADO

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
  print(f'Que pena, você foi repovado com média {m}.')
elif 7.0 > m >= 5.0:
  print(f'Você terá de fazer recuperação, sua média foi de {m}.')
elif m >= 7.0:
  print(f'Você foi aprovado com média {m}. PARABÉNS!')