# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1, -1, -1):
  inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
  print(f'A frase {frase} é um palíndromo.')
else:
  print(f'A frase {frase} não é um palíndromo.')