aluno = dict()
aluno['nome'] = str(input('Nome: ')).title()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é {aluno["nome"]}')
print(f'Média é {aluno["media"]}')
if aluno['media'] >= 7:
    print('Situação é aprovado')
else:
    print('Situação é reprovado')
