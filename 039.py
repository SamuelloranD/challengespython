# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
sexo = str(input('Qual o seu sexo? Responda com "Masculino" ou "Feminino".: ')).strip().upper()
atual = datetime.date.today().year
if sexo == 'MASCULINO':
    nasc = int(input('Em que ano você nasceu? '))
    idade = atual - nasc
    passou = (atual - nasc) - 18 
    falta = 18 - (atual - nasc)
    if passou == 1:
        print('Já passou um ano do seu alistamento.')
    elif passou > 1:
        print(f'Já se passaram {passou} anos do seu ano de alistamento.')
    elif falta > 1:
        print(f'Ainda faltam {falta} anos para o ano do seu alistamento.')
    elif idade == 18:
        print(f'Você deve se alistar neste ano.')
    elif falta == 1:
        print('Falta um ano para o seu alistamento.')
else:
    print('Alistamento não obrigatório.')
