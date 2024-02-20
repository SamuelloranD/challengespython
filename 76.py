# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.


produtos = ('Biscoito', 2.50, 
            'Refrigerante', 5.00, 
            'Feijão', 10.50)
print('~'*40)
print(' '*10, 'LISTAGEM DE PREÇOS')
print('~'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end = '')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('~'*40)        
