def saudacao():
    print("Olá, Mundo!")
    
saudacao()

def recepcao(nome):
    print(f"Olá, {nome}!")
    
recepcao("Joao")
recepcao("Maria")

def soma(a, b):
    return a +b

resultado = soma(3,4)
print(resultado)

quadrado = lambda x: x** 2
print (quadrado(5))

def funcao():
    variavel_local = 10
    print (variavel_local)
    
variavel_global = 20

def funcao2():
    print(variavel_global)
    
funcao()
funcao2()
print(variavel_global)
# print(variavel_local) gera erro pois a variavel não foi definida nesse escopo e sim dentro da função direta

def area_retangulo(base, altura):
    
    """
    Calcula a área de um retângulo.
    
    Args: 
        base (float): A base do retângulo
        altura (float): A altura do retângulo.
        
    Returns:
        float: A área do retângulo.    
    """
    return base * altura

def soma_variavel(*numeros):
    
    total = 0
    for numero in numeros:
        total += numero
    return total
    
print (soma_variavel(1,2, 3))
print(soma_variavel(4, 5, 6, 7))

