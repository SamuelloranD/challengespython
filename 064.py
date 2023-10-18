# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = n = soma = 0
while n != 999:
    n = int(input('Digite um número [999 se quiser parar]: '))
    if n != 999:
        cont += 1
        soma += n
    if n == 999:
        print('Fim.')
print(f'Você digitou {cont} números, a soma entre eles foi {soma}.')
