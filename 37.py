# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número: '))
print('Escolha uma base de conversão')
print('[1] Binário\n[2] Octal\n[3] Hexadecimal')
escolha = int(input('Escolha: '))
if escolha == 1:
    print(f'{n} Convertido em binário é igual a {bin(n)[2:]}')
elif escolha == 2:
    print(f'{n} Convertido em octal é igual a {oct(n)[2:]}')
elif escolha == 3:
    print(f'{n} Convertido em hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente')