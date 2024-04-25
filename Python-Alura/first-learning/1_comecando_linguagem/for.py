# Ensinado FOR com RANGE, CONTINUE, BREAK, sobre a importações random e ABS 

# O FOR normalmente será usado quando você quer definir com qual valor você quer começar, e até qual valor você quer ir e isso é feito também através de uma função que automaticamente que se chamar " RANGE "
# o RANGE define a serie de valores

## o "in" é como se dissesse "dentro" 
import random 

for rodado in range(1,10):
    print(rodado)
    
# ou pulando de dois em dois
print("=-" * 30)

for rodado in range(1,10,2):
    print(rodado)
    
# o JOGO DE ADIVINHAR O NÚMERO

numero_certo = random.randrange(1, 101)
total_de_tentativas = 0
rodada = 1
pontuação = 1000

print("Qual nivel de dificuldade?")
print("(1) Facil (2) Médio (3) Dificil")
nivel = int(input("Define o nível: "))
if(nivel == 1):
    total_de_tentativas = 10
elif(nivel == 2):
    total_de_tentativas = 6
else:
    total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("=-" * 30)
    chute = int(input("\nDigite um número entre 1 e 100: "))
    print("Você digitou:", chute)
    if (chute < 1 or chute > 100):
        print("\033[1;31;47m Algo errado!... siga a regra: digite um valor entre 1 a 100\033[m")
        continue 
    # o CONTINUE também é bastante importante para não parar o programa igual o BREAK, mas voltar ao inicio dele automaticamente.
    print("{}° tentativa , você tem {} chances...".format(rodada, total_de_tentativas))
    if (numero_certo == chute):
        print("\033[1;34;42mVocê acertou e fez {} pontos!\033[m".format(pontos))
        break
    # prestar atenção em como o break é usado
    else:
        if (chute > numero_certo):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (chute < numero_certo):
            print("Você errou! O seu chute foi menor que o número secreto.")
            # o ABS faz com que não venha número negativo da conta abaixo (exemplo -60, passa pra inteiro "60")
        pontos_perdidos = abs(numero_certo - chute)
        pontuação = pontuação - pontos_perdidos
print("Fim de jogo")