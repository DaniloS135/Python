pessoa = {"nome": "Danilo Souza Silva", "idade": 22, "cidade": "São Paulo"}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

#keys(): retorna uma visualização de todas as chaves do dicionário.
#values(): retorna uma visualização de todos os valores do dicionário.
#items(): retorna uma visualização de todos os pares chave-valor do dicionário.
#update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.

individuo = {"nome": "João", "idade": 23, "cidade": "São Paulo"}

print(individuo.keys())

print(individuo.values())

print(individuo.items())

individuo.update({"profissão": "Engenheiro"})
print(individuo)