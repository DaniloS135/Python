nome = input("Digite seu nome: ").strip()

# Loop para garantir que o usuário insira um número válido
while True:
    idade_str = input("Digite sua idade: ").strip()
    if idade_str.isdigit():  # Verifica se a entrada contém apenas números
        idade = int(idade_str)
        break
    print("Erro: Digite uma idade válida em números inteiros!")

while True:
    peso_str = input("Digite seu peso: ").strip()
    try:
        peso = float(peso_str)  # Tenta converter para float
        break
    except ValueError:
        print("Erro: Digite um peso válido em números!")

# Exibindo as informações
print(nome)
print(type(idade))
print(type(peso))
