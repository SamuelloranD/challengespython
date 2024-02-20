# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado.')
    else:
        print('Número duplicado. Não adicionado.')
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
numeros.sort()
print(f'Valores digitados: {numeros}.')
