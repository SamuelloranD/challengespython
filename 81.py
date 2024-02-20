# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
lista.sort(reverse=True)
print('~'*30)
print(f'Foram digitados {len(lista)} números.')
print(f'Números digitados, de forma descrescente: {lista}.')
if 5 in lista:
    print('O valor 5 foi digitado.')
else:
    print('O número 5 não foi digitado.')


