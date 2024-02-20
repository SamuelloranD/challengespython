numeros = [[], []]
c = 0
for n in range(0, 7):
    c = (int(input('Digite um número: ')))
    if c % 2 == 0:
        numeros[0].append(c)
    if c % 2 != 0:
        numeros[1].append(c)
numeros[0].sort()
numeros[1].sort()
print('~'*30)
print(f'Os números pares digitados foram: {numeros[0]}.')
print(f'Os números ímpares digitados foram: {numeros[1]}.')
