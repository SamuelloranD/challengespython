# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

numeros = [int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: '))]
print(f'O maior valor digitado foi {max(numeros)}. Ele apareceu a primeira vez na posição: {numeros.index(max(numeros))}')
print(f'O menor valor digitado foi {min(numeros)}. Ele apareceu a primeira vez na posição: {numeros.index(min(numeros))}')
