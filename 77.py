# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('treze', 'computador', 'teclado', 
            'prato', 'jogos', 'cachorro')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end = '' )
    for letra in p:
        if letra in 'AaEeIiOoUu':
            print(letra, end = ' ')