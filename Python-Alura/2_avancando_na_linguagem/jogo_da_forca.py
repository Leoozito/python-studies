## como definiu o projeto por partes
# enquanto a pessoa não acertar ou nem se enforcou...
# se a pessoa acertar uma letra que tenha na palavra secreta...
# saber a posição...
# saber quais letras foi acertada pelo jogador...
import random 

def jogar_forca():
    
    abertura()
    palavra_secreta = carregando_palavra_aleatoria()
    letras_acertadas = inicia_letras_acertadas(palavra_secreta)
    erros = 0
    enforcou = False 
    acertou = False
    while (not enforcou and not acertou):
        desenha_forca(erros)
        chute = jogador_joga()
        if(chute in palavra_secreta):
            acertar_jogada(chute, letras_acertadas, palavra_secreta)
        else:
            erros = erros + 1
        # amostra do final do jogo
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)  
        
        if(acertou):
            print("Você ganhou !")
        else:
            print("Você perdeu !")
    print("Fim do jogo")
    
def abertura():
    print("=-" * 20)
    print("BEM VINDO AO JOGO DA FORCA")
    print("=-" * 20)
    
def carregando_palavra_aleatoria():
    palavras = []
    
    # acessando o arquivo
    arquivo = open("palavras.txt", "r")
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha) 
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicia_letras_acertadas(palavra):
    lista = ["_" for letra in palavra]
    return lista
    # exemplo de duas linhas de codigos com for, trocada pelo exemplo de cima
    # for letra in palavra_secreta:
    #     letras_acertadas.append("_")

def jogador_joga():
    chute = input("Diga qual letra?...")
    chute = chute.strip().upper()
    return chute

def acertar_jogada(chute, letras_acertadas, palavra_secreta):
    index = 0
    
    for letra in palavra_secreta:
        #logo depois de tratar a letra sem espaços, passa para maiuscula os dois lados para fazer a comparação
        if (chute == letra):
            letras_acertadas[index] = letra
        index = index + 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar_forca()

# ------------------------------------------------------------------------------
# algumas funções ======== no python temos...
## o .OPEN("palavras.txt", "w") que primeiro vc define o arquivo, em segundo você passa uma letra padronizadas com funções em si próprias, por exemplo: " w " para abrir em modo de escrita, modo leitura é o " r ", " a " para acrescentar conteudo. O .CLOSE() fecha o arquivo. .WRITE() adiciona coisas dentro do arquivo.