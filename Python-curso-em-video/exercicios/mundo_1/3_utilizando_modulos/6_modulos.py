#                       EXERCICIO 16
import math
import random

numReal = float(input("Digite qualquer número do tipo real: "))
numInt = math.trunc(numReal)
print(f"O numero passado em sua versão inteira é {numInt}")
print("-----------------------------------------------------\n")

#                       EXERCICIO 17
## código de calculo da hipotenusa : MANUAL
catOposto = float(input("Valor do Cateto Oposto: "))
catAdjac = float(input("Valor do Cateto Adjacente: "))

hipotenusa = (catAdjac ** 2 + catOposto ** 2) ** (1/2) # para calcular raiz quadrada de um numero tem que ter o " 1/2 "

print(f"O resultado da hipotenusa é {hipotenusa}")

## código de calculo da hipotenusa: com ajuda do pacote do Python
hipotenusa2 = math.hypot(catOposto, catAdjac)
print(f"O resultado da hipotenusa do jeito que o PYTHON calcula é {hipotenusa2}")
print("-----------------------------------------------------\n")

#                       EXERCICIO 18
angulo = float(input("Digite o angulo que você deseja: "))

seno = math.sin(math.radians(angulo))
print("O angulo de {} tem o SENO de {:.2f}".format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print("O angulo de {} tem o COSSENO de {:.2f}".format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print("O angulo de {} tem o TANGENTE de {:.2f}".format(angulo, tangente))
print("-----------------------------------------------------\n")

#                       EXERCICIO 19

aluno1 = str(input("Primeiro Aluno: "))
aluno2 = str(input("Segundo Aluno: "))
aluno3 = str(input("Terceiro Aluno: "))
aluno4 = str(input("Quarto Aluno: "))
todosAluno = [aluno1, aluno2, aluno3, aluno4]

alunoEscolhido = random.choice(todosAluno)
print("O(a) aluno(a) escolhido(a){}".format(alunoEscolhido))
print("-----------------------------------------------------")
