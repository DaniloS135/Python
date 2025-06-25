class Pessoa:
    "Isto é uma nova classe chamada Pessoa"
    
    def __init__(self, nome):
        self.nome = nome
        self.idade = input("Digite a sua idade:")
        
    def saudacao(self):
        print(f"Olá {self.nome}!")

'''print(Pessoa.idade)

print(Pessoa.saudacao)

print(Pessoa.__doc__)'''

nome_input = input("Digite seu nome:")
pessoa = Pessoa(nome_input)
pessoa.saudacao()

