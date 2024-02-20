# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média

nome = input('Digite o seu nome: ')
disciplina = input('Digite o nome da disciplina: ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
s = n1 + n2

print(f'Olá, {nome}, sua média na disciplina de {disciplina} foi de {s/2}.')
