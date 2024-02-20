from time import sleep


def maior(* núm):
    cont = maior = 0
    print('Analisando os valores...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores, e o maior foi: {maior}')

def linha():
    print('-=' * 20)

maior(2, 9, 4, 5, 7, 1)
linha()
maior(1, 2)
linha()
maior(6)
linha()
maior()
