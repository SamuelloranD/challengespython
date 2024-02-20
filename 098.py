from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',  end='', flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
    print('FIM!')


# PROGRAMA PRINCIPAL
contador(0, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é com você! ')
início = int(input('Início: '))
final = int(input('Final: '))
passo = int(input('Passo: '))
contador(início, final, passo)
