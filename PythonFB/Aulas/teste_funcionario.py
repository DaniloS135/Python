from funcionario import Funcionario

funcionario = Funcionario('Danilo', 'danilosouza@blabla.com')

funcionario.cadastro_hora('Jan', 200)
funcionario.cadastro_hora('Fev', 250)
funcionario.cadastro_salario('Jan', 35)
funcionario.cadastro_salario('Fev', 30)

print(funcionario)
print(funcionario.calcula_salario('Jan'))
print(funcionario.calcula_salario('Fev'))
