# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()
f1 = frase.count('A')
f2 = frase.find('A')+1
f3 = frase.rfind('A')+1
print(f'A letra A aparece {f1} vezes na frase.')
print(f'A letra A apareceu na posição {f2}.')
print(f'A letra A pareceu pela última vez na posição {f3}.')
