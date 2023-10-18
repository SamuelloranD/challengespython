# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

total = int(input('Quanto você quer sacar? R$'))
cédula = 50
total_cédulas = 0
while True:
    if total >= cédula:
        total -= cédula
        total_cédulas += 1
    else:
        if total_cédulas > 0:
            print(f'Total de {total_cédulas} cédulas de R${cédula}.')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 2
        total_cédulas = 0
        if total == 0:
            break