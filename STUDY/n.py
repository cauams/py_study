# For Loops p/ números

inicio = input('Indique o número inicial: ')
inicio = int(inicio)

fim = input('Indique o número final: ')
fim = int(fim)

pulos = input('Indique de quanto em quanto é para o computador pular: ')
pulos = int(pulos)

# imprimir de 1 até quanto você quiser!

for numero in range(inicio, fim, pulos):
    print(numero)
