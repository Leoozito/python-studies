# Ensinado sobre a variavel __name__

# o JOGO DE ADIVINHAR O NÚMERO
import random

def jogar_adivinhacao() :
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

# O __name__ é que torna o "jogar()" no exemplo abaixo, como o 'MAIN' dos arquivo

# a utilidade dele é quando você está construindo projetos maiores, você divide as funções as classes e as coisas que está sendo construidas, em arquivos diferentes. Isso permite que eu consiga fazer teste, executando funções especificas definidas no __name__.
if(__name__ == "__main__"):
    jogar_adivinhacao()