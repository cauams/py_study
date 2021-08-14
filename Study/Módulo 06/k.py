# While Loop

# Bom para loops que dependem de uma condição

# EX: Criar uma promoção que diminui o valor de um produto que custa 100 reais gradativamente. até 30 reais, para manter 10 reais de lucro.

preco = 100
dia = 0

while preco > 25:
    dia += 1
    print(f'No dia {dia}, o valor do produto irá ser R${float(preco)}')
    preco -= 5
    