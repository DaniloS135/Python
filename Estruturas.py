try:
    idade = int(input("Qual a sua idade?").strip())
    if idade >= 18:
            print ("Você é maior de idade.")
    else:
            print("Você é menor de idade.")
except ValueError:
    print("Por favor, digite um número válido.")