# For loop, criar um retângulo

# objetivo: fazer um retângulo y x y 

linhas = input('Escolha a quantidade de linhas: ')
colunas = input('Escolha a quantidade de colunas: ')
linhas = int(linhas)
colunas = int(colunas)


simbolo = '#'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()