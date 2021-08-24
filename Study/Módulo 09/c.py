# Erros, else e finally

try:
    idade = int(input('Digite a sua idade: '))
    print(idade)
except ValueError:
    print('Por favor digite um número!')
else:
    print('Registrando a sua idade!')
finally:
    print('Redirecionando...')