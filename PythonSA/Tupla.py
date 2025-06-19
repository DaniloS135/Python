ponto = (3,4)

print (ponto [0])
print (ponto [1])


#count(elemento): devolve o número de vezes que um elemento aparece na tupla.
#index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 
#len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.

minha_tupla = (1, 2, 3, 2, 4, 2)

print (minha_tupla.index(2))
print (minha_tupla.index(2, 2))
print (minha_tupla.index(2, 2, 4))
