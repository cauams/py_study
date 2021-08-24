# Python OOP, iniciando em classes.

    # Criando construtores.


# Cria a classe
class Funcionarios:
    # Cria o construtor
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
    # Cria a função de juntar o nome ao sobrenome
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

# Cria os objetos

func1 = Funcionarios('Caua', 'de Miranda', '24/10/200X')
func2 = Funcionarios('Lucas', 'Silva', '09/02/199X')

# Prints

print(Funcionarios.nome_completo(func1))
print(func1.data_nascimento)

print(Funcionarios.nome_completo(func2))
print(func2.data_nascimento)

print() # ou:

print(func1.nome_completo())
print(func2.nome_completo())
