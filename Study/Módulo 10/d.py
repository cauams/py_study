# Python OOP, iniciando em classes.

from datetime import datetime


# Cria a classe
class Funcionarios:
    # Cria o construtor
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    # Cria a função de juntar o nome ao sobrenome

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    # Cria a função para calcular a idade do nascimento

    def idade_func(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

# Cria os objetos


func1 = Funcionarios('Caua', 'de Miranda', 2003)
func2 = Funcionarios('Lucas', 'Silva', 1998)

# Prints

print(Funcionarios.nome_completo(func1))
print(Funcionarios.idade_func(func1))

print(Funcionarios.nome_completo(func2))
print(Funcionarios.idade_func(func2))
