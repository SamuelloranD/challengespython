def escreva():
    tam = len(palavra) + 4
    print('~' * tam)
    print(f'  {palavra}')
    print('~' * tam)


# PROGRAMA PRINCIPAL
palavra = str(input('Digite algo: '))
escreva()