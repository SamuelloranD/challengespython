# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
  n1 = int(input('Digite um número: '))
  if n1 % 2 == 0:
    soma += n1
    cont += 1
print(f'A soma dos números pares digitados é igual a: {soma}.')