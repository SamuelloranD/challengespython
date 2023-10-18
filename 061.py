# Refazendo o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end = '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end = '')
    t1 = t2
    t2 = t3
    cont += 1
