# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato. 

total = maior1000 = cont = menor = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        maior1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total gasto foi de R${total:.2f}.')
print(f'Total de produtos que custam mais de R$1000,00: {maior1000}.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}.')
