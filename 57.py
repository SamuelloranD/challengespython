# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Qual o seu sexo? Responda com 'M ou F'. ")).upper().strip()
while sexo not in 'MmFf':
  print('Tente novamente.')
  sexo = str(input("Qual o seu sexo? Responda com 'M ou F'.")).upper().strip()
if sexo == 'M':
  print('Ok, você é do sexo Masculino.')
elif sexo == 'F':
  print('Ok, você é do sexo Feminino.')