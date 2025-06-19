def funcao():
    if condicao: # type: ignore
        raise Exception("Descrição de erro")
    # Código que pode gerar uma exceção personalizada
   
try:
    funcao()    
except Exception as e:
    print(f"Erro: {str(e)}")

"""
except Exception as e:
Exception:
É a classe base de quase todos os erros em Python. Isso quer dizer que esse except vai capturar qualquer exceção, desde que ela herde de Exception.

as e:
Aqui, você está salvando a exceção capturada na variável e.
Isso permite que você acesse informações sobre o erro que ocorreu.

print(f"Erro: {str(e)}")
Esse print usa uma f-string, que é uma forma moderna e prática de formatar strings no Python (disponível desde o Python 3.6).

f"..." → f-string
Ao colocar um f antes das aspas, você diz ao Python que aquela string pode conter expressões entre chaves {} que serão avaliadas e inseridas automaticamente no texto.

{str(e)}
Aqui, você está convertendo o objeto da exceção (e) para string com str(e), para que ele mostre a mensagem de erro.

Exemplo: se a exceção for ValueError("Entrada inválida"), o str(e) resultará em "Entrada inválida".

"""
    
    