"""
try:
    idade = int(input("Qual a sua idade?").strip())
    if idade >= 18:
            print ("Você é maior de idade.")
    else:
            print("Você é menor de idade.")
except ValueError:
    print("Por favor, digite um número válido.")"""

nota = int(input("Qual sua nota? "))

if nota>= 90:
    print ("Excelente")

elif nota >= 80:
    print ("Muito bom")

elif nota >= 70:
    print ("Bom")

else:
    print ("Precisa melhorar")
    
