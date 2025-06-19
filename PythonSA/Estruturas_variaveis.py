#Listas
frutas = ["maçã", "banana", "laranja"]

print(frutas[0]) #Imprime "maçã"
print(frutas[1]) #Imprime "banana"
print(frutas[2]) #Imprime "laranja"

"""
append(elemento): adiciona um elemento ao final da lista.
insert(indice, elemento): insere um elemento em uma posição específica da lista.
remove(elemento): remove a primeira ocorrência de um elemento na lista.
pop(indice): remove e retorna o elemento em uma posição específica da lista.
sort(): ordena os elementos da lista em ordem ascendente.
reverse(): inverte a ordem dos elementos na lista.
"""

frutas.append("pera")
print(frutas) #Imprime ["maçã", "banana", "laranja", "pera"]
frutas.insert(1, "uva")

frutas. remove("banana")

fruta_removida = frutas.pop(2)

frutas.sort()

frutas.reverse()