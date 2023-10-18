# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: À vista dinheiro/cheque: 10% de desconto; À vista no cartão: 5% de desconto; Em até 2x no cartão: preço formal; 3x ou mais no cartão: 20% de juros

print(f'{"LOJA GENÉRICA":=^40}')
produto = float(input('Digite o preço do produto: R$'))
print('''Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual a opção desejada? '))
if opção == 1:
  d1 = produto - (produto * 0.1)
  print(f'Com o desconto aplicado, o valor a ser pago é de R${d1:.2f}.')
elif opção == 2:
  d2 = produto - (produto * 0.05)
  print(f'Com o desconto aplicado, o valor a ser pago é de R${d2:.2f}.')
elif opção == 3:
  d3 = produto / opção
  print(f'O valor a ser pago é de R${produto:.2f} parcelado em {opção} vezes.')
elif opção == 4:
  parcelas = int(input('Em quantas parcelas? '))
  d4 = produto + (produto * 0.2)
  print(f'O valor a ser pago é de R${d4:.2f} parcelado em {parcelas} vezes de R${d4/parcelas:.2f}.')