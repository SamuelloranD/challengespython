# Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada.

import random
n1 = input('Digite o nome do aluno 1 ')
n2 = input('Digite o nome do aluno 2 ')
n3 = input('Digite o nome do aluno 3 ')
n4 = input('Digite o nome do aluno 4 ')
lista = [n1, n2, n3, n4]
sorteado = random.choice(lista)
random.shuffle(lista)
print(f'A ordem de apresentação será: {lista}.')