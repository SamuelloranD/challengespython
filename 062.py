# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

n1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
termos = 10
while termos != 0:
    while termos != 0:
        print(f'{n1} -> ', end='')
        n1 += r
        termos -= 1
    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar a mais? '))
