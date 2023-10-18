# Faça um programa que leia o preço de um produto e mostre seu novo preço após 5% de desconto.

p = float(input('Qual o preço original do produto? '))
a = 0.05 * p
print(f'O preço após desconto de 5% será de {p - a:.2f} reais')
