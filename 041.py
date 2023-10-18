# Faça um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos: MIRIM; Até 14 anos: INFANTIL; Até 19 anos: JÚNIOR; Até 25 anos: SÊNIOR, Acima de 25 anos: MASTER.

import datetime
atual = datetime.date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
if idade <= 9:
  print(f'Você tem {idade} anos.')
  print('Você é da categoria MIRIM.')
elif idade > 9 and idade < 15:
  print(f'Você tem {idade} anos.')
  print('Você é da categoria INFANTIL.')
elif idade > 14 and idade < 20:
  print(f'Você tem {idade} anos.')
  print('Você é da categoria JUNIOR.')
elif idade == 20:
  print(f'Você tem {idade} anos.')
  print('Você é da categoria SÊNIOR.')
elif idade > 20:
  print(f'Você tem {idade} anos.')
  print('Você é da categoria MASTER.')
