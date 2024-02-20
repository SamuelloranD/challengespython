# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = [] 
while True:
    n = (int(input('Digite um número: ')))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {lista_par}.')
print(f'A lista de ímpares é {lista_impar}.')
