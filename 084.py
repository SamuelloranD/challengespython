pessoas = []
dados = []
cont = maior = menor = 0
while True:
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(float(input('Digite o seu peso: kg')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    continuar = str(input('Deseja adicionar mais pessoas? [S/N] '))
    cont += 1
    pessoas.append(dados[:])
    dados.clear()
    
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {cont} pessoas')
for p in pessoas:
    if p[1] == maior:
        print(f'O maior peso foi de {p[0]}.')
for p in pessoas:
    if p[1] == menor:
        print(f'O menor peso foi de {p[0]}.')
