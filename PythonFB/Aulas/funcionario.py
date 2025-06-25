class Funcionario:
    def __init__(self, nome, email, horas_trabalhadas):
        self.nome = nome
        self.email = email
        self.horas_trabalhadas = horas_trabalhadas
    
    def exibir_dados(self):
        print("\n=== Dados do Funcionário===")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Horas Trabalhadas: {self.horas_trabalhadas}")
        
nome = input('Digite o seu nome:')
email = input('Digite o seu e-mail:')
horas = input('Digite as suas horas trabalhadas:')

funcionario = Funcionario(nome, email, horas)

funcionario.exibir_dados()

        
        
        

        
    