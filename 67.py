# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

while True:
    n = int(input('Digite um número para ver a sua tabuada: '))
    if n < 0:
        print(f'Fim. Você digitou um número negativo.')
        break
    for n1 in range(1, 10):
        print(f'{n} x {n1} = {n*n1}') 
    print('~' * 30)