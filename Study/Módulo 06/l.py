# Condições em While Loops

# Publicar um produto com comissão de 10% se for acima de 20 reais.

valor = int(input('Digite o valor do seu produto: '))

while valor > 20:
    valor = valor + (valor * 0.10)
    print(f'O valor final do seu produto será de R${valor}')
    break
else:
    print(f'O valor final do seu produto será de R${valor}')