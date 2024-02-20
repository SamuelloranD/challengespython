números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n1 = int(input('Digite um número entre 0 e 20 para ver o seu extenso: '))
while n1 > 20 or n1 < 0:
    print('O número digitado não está entre 0 e 20. Tente novamente.')
    n1 = int(input('Digite um número entre 0 e 20 para ver o seu extenso: '))
print(f'Você digitou o número {números[n1]}.')
