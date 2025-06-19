#try
try:
    # Código que pode gerar uma exceção
 resultado = 10/0
 print(resultado)
except ZeroDivisionError:
 print("Erro: Divisão por Zero")
except ValueError:
    print("Erro: Valor Inválido")


#O bloco finally é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não. É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.

arquivo = None
try:
    arquivo = open("arquivo.txt", "r")
    #realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo Não Encontrado")     
finally: 
    if arquivo:
        arquivo.close() #Dessa forma garante que só tenta fechar o arquivo se for aberto com sucesso.
    
