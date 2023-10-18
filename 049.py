# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

from time import sleep 
n1 = int(input('Digite um número para descobrir sua tabuada: '))
for c in range(n1, n1*10, n1):
  print(c)
  sleep(1)
