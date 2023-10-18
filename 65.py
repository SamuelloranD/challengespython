# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
cont = soma = média = maior = menor = 0
while resp in 'Ss':
    n = int(input("Digite um número: "))
    soma += n
    cont += 1
    média = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
if resp in 'Nn':
    print('Fim')
print(f'Você digitou {cont} números')
print(f'A soma entre eles foi {soma}')
print(f'A média entre eles foi {média:.2f}')
print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}') 