velocidade = input('Qual a velocidade do carro? ')
velocidade = int(velocidade)

if velocidade > 110:
    print('Você está acima da velocidade permitida!')
    print('Multa aplicada')
elif velocidade < 60:
    print('Por favor, dirija mais rápido!')
else:
    print('Você está na velocidade adequada!')
