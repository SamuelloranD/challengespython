# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
terceira_coluna = 0
maiorsegunda_linha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            terceira_coluna += matriz[l][c]
        if matriz[1][c] > maiorsegunda_linha:
            maiorsegunda_linha = matriz[1][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares digitados é igual a: {soma_pares}.')
print(f'A soma dos valores da terceira coluna é igual a: {terceira_coluna}.')
print(f'O maior valor da segunda linha é: {maiorsegunda_linha}.')
