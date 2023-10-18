# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

c1 = float(input('Qual o valor da casa que você deseja comprar? R$'))
s1 = float(input('Qual o seu salário? R$'))
a1 = int(input('Em quantos anos você pretende pagar? '))
a2 = a1 * 12
p = c1 / a2
print(f'O valor da prestação será de R${p:.2f}.')
if p > 0.3 * s1:
  print('Empréstimo NEGADO.')
else:
  print('Empréstimo CONCEDIDO.')
