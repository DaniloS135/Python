import math

resultado = math.sqrt(25)
print(resultado)

#Neste exemplo, importa-se o módulo math utilizando a declaração import. Em seguida, utiliza-se a função sqrt() do módulo math para calcular a raiz quadrada de 25.

from math import sqrt

resultado2 = sqrt(49)
print(resultado2)

#Neste caso, importa-se apenas a função sqrt() do módulo math, o que nos permite utilizá-la diretamente sem ter que precedê-la com o nome do módulo.

#Math, Fornece funções matemáticas, como sqrt() (raiz quadrada), sin() (seno), cos() (cosseno), entre outras.
#Random, Oferece funções para gerar números aleatórios, como random() (número aleatório entre 0 e 1), randint() (número inteiro aleatório em um intervalo), entre outras.
#Datetime, Permite trabalhar com datas e horas, como datetime.now() (data e hora atual), datetime.date() (data), datetime.time() (hora), entre outras.

import random
import datetime

numero_aleatorio = random.randint(5,10)
print(numero_aleatorio)

data_atual = datetime.datetime.now()
print(data_atual)

