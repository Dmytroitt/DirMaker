import os
nome = str(input('Insira o nome para os diretórios: '))
quantidade = int(input('Insira a quantidade de diretórios que deseja criar: '))
for i in range(0, quantidade):
    os.mkdir(r'{}{:03d}'.format(nome,i))
print('Diretórios criados!')
