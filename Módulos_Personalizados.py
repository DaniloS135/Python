#Para criar um módulo personalizado, simplesmente criamos um novo arquivo Python com o nome desejado e definimos as funções, classes e variáveis que queremos incluir no módulo.

import meu_modulo

meu_modulo.saudar("João")

resultado = meu_modulo.calcular_soma(5,3)
print(resultado)

import meu_modulo

resultado1 = meu_modulo.somar(5,3)
meu_modulo.imprimir_mensagem(f"O resultado da soma é: {resultado1}")

nome = meu_modulo.obter_nome_usuario()
meu_modulo.imprimir_mensagem(f"Olá, {nome}!")



