# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
num = int(input('Tente adivinhar um número de 1 a 5: '))
n1 = [1, 2, 3, 4, 5]
n2 = random.choice(n1)
if num == n2:
  print('Parabéns, você acertou!')
else:
  print(f'Que pena, você errou, o número correto era {n2}.')
