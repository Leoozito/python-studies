#                   CORES NO TERMINAL

# método ANSI é o que faz colocar cor, usando por exemplo "\033[m " , vo^ce adiciona números entre o colchete e o "m" para definir como vai querer a cor

# para definir a letra tem 3 meios, para ser colocado números padronizados.

# eles são STYLE (primeiro a ser definido por numero): 0 -> None ; 1 -> Bold ; 4 -> Underline ; 7 -> Negative

# TEXT : 30 -> Branco ; 31 -> Vermelho ; 32 -> Verde ; 33 -> Amarelo; 34 -> Azul ; 35 -> Roxo; 36 -> Ciano ; 37 -> Cinza; 

# BACK : mesmas cores na ordem de cima só que ao invés de 30 é -> 40-47

#EXEMPLO
 
print("\033[1;31;43mOlá, Mundo!\033[m")
print("-"* 40)

nome= 'Leonardo'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m',}

print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['azul'], nome, cores['limpa']))