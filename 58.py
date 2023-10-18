# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from time import sleep
from random import randint
nome = str(input('Digite o seu nome: ')).capitalize()
sleep(1)
t = 0
computador = randint(1, 10)
num = int(input('Tente adivinhar um número entre 1 e 10 que foi escolhido pelo computador: '))
while num != computador:
  t += 1
  num = int(input('Tente outro número. ')) 
if num == computador:
  t += 1
  print(f'Parabéns, {nome}, você acertou o número escolhido pelo computador. Você precisou de {t} tentativas.')