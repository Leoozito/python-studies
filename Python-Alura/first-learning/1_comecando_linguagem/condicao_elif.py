numero_secreto = 42

chute = input("Digite o seu numero: ")

print("Você digitou ", chute)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")
        
print("Fim de jogo")