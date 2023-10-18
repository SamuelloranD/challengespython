# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas; Quantas letras ao todo (sem considerar espaços); Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome ')).strip()
nome2 = nome.upper()
nome3 = nome.lower()
print(nome2)
print(nome3)
print(len(nome)-nome.count(' '))
nome4 = nome.find(' ')
print(f'Seu primeiro nome tem {nome4} letras.')
