#Entrada

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))

if idade >= 18:
    status = "maior de idade"
    
else:
    status = "menor de idade"

#Saída
print(f"Olá, {nome}! Você é {status} e tem {idade} anos.")

#Neste exemplo, solicita-se ao usuário que insira seu nome e idade utilizando a função input(). Os valores inseridos são armazenados nas variáveis nome e idade, respectivamente. Em seguida, essas variáveis são utilizadas para mostrar uma saudação personalizada na tela.
#Utilizei o int na variavel da idade e coloquei if-else para identificar se a pessoa será maior ou menor de idade, no print juntei as duas variáveis e personalizei 2 mensagens para as possiveis opções.
#Utilizei a f-string (formatação de cadeias) para inserir variáveis diretamente dentro de uma cadeia de texto.



