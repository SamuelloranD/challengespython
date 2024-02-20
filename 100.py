from random import randint
from time import sleep

números = list()

def sorteia():
    print('Sorteando 5 valores: ', end='')
    sleep(0.5)
    for c in range(0, 5):
        nums = randint(0, 5)
        print(f'{nums} ', end='', flush=True)
        sleep(0.5)
        números.append(nums)

def somaPar():
    pares = 0
    for c in números:
        if c % 2 == 0:
            pares += c
    print(f'\nA soma dos números pares da lista {números} é igual a {pares}.')


# PROGRAMA PRINCIPAL
sorteia()
somaPar()