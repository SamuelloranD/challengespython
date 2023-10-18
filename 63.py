# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
contador = 3
print(f'{t1} -> {t2}', end='')
while contador <= n:
    t3 = t1 + t2
    print(f' -> {t3}',end='')
    t1 = t2
    t2 = t3
    contador+=1
print(' -> FIM')