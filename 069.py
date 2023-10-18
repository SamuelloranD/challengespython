# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos. 

homens = maior = mulhermenor = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 18:
        mulhermenor += 1
    print('~' * 30)
    continuar = str(input('Deseja cadastras uma nova pessoa? [S/N] ')).upper().strip()[0]
    print('~' * 30)
    if continuar != 'S':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}.')
print(f'Total de homens cadastrados: {homens}.')
print(f'Total de mulheres com menos de 20 anos: {mulhermenor}.')
