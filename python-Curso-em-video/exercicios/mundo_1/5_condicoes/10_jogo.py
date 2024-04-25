#                       EXERCICIO 28

import random

numDoUsuario = int(input("Tecle um numero de 0 a 5: "))
print(f"Você teclou o número [ {numDoUsuario} ]")

numDoPC = random.randint(0, 5)

print(f"O computador jogou [ {numDoPC} ]")

if numDoUsuario == numDoPC:
    print("\nVOCÊ ACERTOU !! FANTASTICO")
else: 
    print("Errouu, tente novamente")
    