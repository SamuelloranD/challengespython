grupo = list()
pessoa = dict()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO. Digite M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda com S ou N.')
    if continuar == 'N':
        break
print(grupo)


