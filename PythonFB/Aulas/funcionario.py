class Funcionario:
    def __init__(self, nome, email, horas_trabalhadas, salario):
        self.nome = nome
        self.email = email
        self.horas_trabalhadas = horas_trabalhadas
        self.salario = {}
    
    def exibir_dados(self):
        print("\n=== Dados do Funcionário===")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Horas Trabalhadas: {self.horas_trabalhadas}")
        
    def cadastro_hora(self, mes, horas_trabalhadas):
        if (mes not in self.horas_trabalhadas):
            self.horas_trabalhadas[mes] = horas_trabalhadas
    
    def cadastro_salario(self, mes, valor):
        if (mes not in self.salario):
            self.salario[mes] = valor
    
    def calcula_salario(self, mes):
        if (mes not in self.horas_trabalhadas) or (mes not in self.salario):
            print ("Mês Inexistente!!")
        else:
            return self.horas_trabalhadas[mes] * self.salario[mes]
        
    def __repr__(self):
        return f"Funcionário: {self.nome}, \nEmail: {self.email}, \nhoras/mês: {self.horas_trabalhadas}, \nsalário-hora: {self.salario}"
    
        
        
nome = input('Digite o seu nome:')
email = input('Digite o seu e-mail:')
horas = input('Digite as suas horas trabalhadas:')

funcionario = Funcionario(nome, email, horas)

funcionario.exibir_dados()

        
        
        

        
    