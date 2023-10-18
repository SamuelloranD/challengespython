# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Qual o valor do seu salário? R$'))
if s > 1250.00:
  s2 = s * 0.10
  print(f'Seu novo salário, após o aumento, será de R${s2 + s:.2f}.')
else:
  s3 = s * 0.15
  print(f'Seu novo salário, após aumento, será de R${s3 + s:.2f}.')
