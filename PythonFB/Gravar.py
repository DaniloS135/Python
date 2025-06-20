arquivo = open("arqText.txt", "w")

arquivo.write('Curso Pyhton \n')
arquivo.write('Aula Pratica')
arquivo.close()

#leitura do arquivo texto

leitura = open('arqText.txt', 'r')
print (leitura.read())
leitura.close