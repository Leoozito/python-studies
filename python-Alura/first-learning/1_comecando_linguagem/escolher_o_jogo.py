from jogo_1 import jogar_adivinhacao
from jogo_2 import jogar_forca

def escolhe_jogo():
    print("=-" * 20)
    print("ESCOLHA O SEU JOGO")
    print("=-" * 20)

    print("(1) Forca (2) Adivinhar")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogando forca")
        jogar_forca()
    elif (jogo == 2):
        print("Jogando adivinhação")
        jogar_adivinhacao()
        
if(__name__ == "__main__"):
    escolhe_jogo()