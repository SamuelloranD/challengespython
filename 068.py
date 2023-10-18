# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint 
v = 0
while True:
    computador = randint(0, 10)
    p = str(input('Par ou ímpar? [I/P] ')).upper().strip()
    n = int(input('Digite um número de 0 a 10: '))
    if p == 'P':
        if (computador + n) % 2 == 0:
            print(f'Você escolheu Par. Computador jogou {computador} e você jogou {n}. Portanto: ')
            print('Você venceu.')
            v += 1
        elif (computador + n) % 2 != 0:
            print(f'Você escolheu Par. Computador jogou {computador} e você jogou {n}. Portanto: ')
            print('Você perdeu.')
            break
    if p == 'I':
        if (computador + n) % 2 != 0:
            print(f'Você escolheu ímpar. Computador jogou {computador} e você jogou {n}. Portanto: ')
            print(f'Você venceu.')
            v += 1
        if (computador + n) % 2 == 0:
            print(f'Você escolheu ímpar. Computador jogou {computador} e você jogou {n}. Portanto: ')
            print('Você perdeu.')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes.')
