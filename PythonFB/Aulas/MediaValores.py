qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd  = qtd + 1
    #Entrada de valores
    valor = float(input("Digite um valor: "))
    
#caso digite um valor negativo o laço encerra

media = soma / qtd

print("Total da Soma: ", soma) 
print("Quantidade de valores digitados: ", qtd )
print("Média dos valores: ", media)
    