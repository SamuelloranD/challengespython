# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

from time import sleep
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    somaidade += idade
    sexo = str(input('Digite o seu sexo: ')).upper()   
    if p == 1 and sexo in 'Mm':
        maioridadehomem == idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += +1
médiaidade = somaidade / 4
print('Analisando o grupo de pessoas informado... ')
sleep(3)            
print(f'A média de idade dessas pessoas é de {médiaidade:.1f} anos.')
sleep(1)
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
sleep(1)
print(f'{totmulher20} mulheres têm menos de 20 anos.')    