# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos quilômetros foram percorridos com o veículo? '))
d = float(input('Por quantos dias o veículo foi alugado? '))
v1 = 0.15 * km
v2 = 60 * d
print(f'O valor a ser pago é de R${v1+v2:.2f}.')