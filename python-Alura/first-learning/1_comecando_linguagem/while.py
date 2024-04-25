# o while seria o "enquanto", com ele se começa a fazer repetições 
# No exemplo faz com que o usuário tenha um limite de tentativa com a ajuda do WHILE, evitando o ctrl C ctrl V

numero_certo = 42
total_de_tentativas = 3
rodada = 1

while (total_de_tentativas >= 0):
    chute = int(input("Digite o seu numero: "))
    print("Você digitou:", chute)
    
    print(f"{rodada}° tentativa")
    if (numero_certo == chute):
        print("Você acertou!")
    else:
        if (chute > numero_certo):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (chute < numero_certo):
            print("Você errou! O seu chute foi menor que o número secreto.")
    
    total_de_tentativas =  total_de_tentativas - 1
    rodada = rodada + 1    
print("Fim de jogo")