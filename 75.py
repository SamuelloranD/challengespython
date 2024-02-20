# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9.B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

numeros = (int(input('Digite o primeiro número: ')), int(input('Digite o primeiro número: ')),
     int(input('Digite o primeiro número: ')), int(input('Digite o primeiro número: ')))
print(f'O número 9 apareceu {numeros.count(9)} vez(es).')
if 3 in numeros:
    posicao_tres = (numeros.index(3)+1)
    print(f'O número 3 apareceu a primeira vez na posição {posicao_tres}.')
else: 
    print('O número 3 não apareceu nenhuma vez.')
print('Os valores pares digitados foram: ', end = '')
for n in numeros:
    if n % 2 == 0:
        print(n, end = ' ')

