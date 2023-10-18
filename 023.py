# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

from time import sleep
n1 = int(input('Digite um número de 4 dígitos: '))
n2 = str(n1)
print(f'Anlisando o número {n1}')
sleep(1)
print(f'Unidade: {n2[3]}')
print(f'Dezena: {n2[2]}')
print(f'Centena: {n2[1]}')
print(f'Milhar: {n2[0]}')
