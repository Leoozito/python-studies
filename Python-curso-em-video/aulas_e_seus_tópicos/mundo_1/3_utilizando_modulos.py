# MODULOS - TEORICO

## Fazer importações de pacotes no Python

# Vejamos por exemplo que o Python tem um pacote ja instalado nele, chamado " math " 
# E no math tem varias propriedades, como CEIL que faz arredondamento, tem o FLOOR que arredonda pra baixo, tem o TRUNC que elimina os numeros que vem depois da virgula, o POW que é potencia, SQRT de calcular raiz quadrada,e tem o FACTORIAL para calcular fatorial.
# Pegando como base de exemplo esse pacote do Python, para importar fazemos assim:
# Para importar todas essas funções:        import math
# Importar função especifica:               from math import sqrt

# PRATICA

from math import sqrt, ceil
import random # random nos entrega números aleatórios
import emoji

num = int(input("Digite um número "))
raiz = sqrt(num)
print(f"a raiz de {num} é {ceil(raiz)}") # com o from não precisa colocar o ' math. '

num = random.randint(1, 10) # gera numero aleatorio (com padrão definido)
print(num)

print(emoji.emojize("Olá Mundo :alien:"))