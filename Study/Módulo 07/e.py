# xargs indentificando os parametros.

    # ** -> Vários parametros com argumentos.


def agencia(**carro):
    return carro

print(agencia(marca='Chevet', cor='preto', motor='4 tempos v8', placa='XMW4192'))