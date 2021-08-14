# For Loops Usando IF e ELSE

buy_confirmation = True
data = "Compra no valor de R$20.00 e entrega confirmada"

for solicitar in range(3):
    if buy_confirmation:
        print(data)
        print('Detalhes da compra enviados para o seu e-mail.')
        break
else:
    print('Falha na compra!')

