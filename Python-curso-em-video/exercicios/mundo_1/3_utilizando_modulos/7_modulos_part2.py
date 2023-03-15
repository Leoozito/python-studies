#                           EXERCICIO 20
import random
# import pygame

nome1 = input("Digite o nome da 1° pessoa: ")
nome2 = input("Digite o nome da 2° pessoa: ")
nome3 = input("Digite o nome da 3° pessoa: ")
nome4 = input("Digite o nome da 4° pessoa: ")

lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista) # A função do shuffle é ' embaralhar ' de modo aleatório
print("\nQuem chegou em 1°, 2°, 3°, 4° colocado")
print(lista)
print("-----------------------------------------------")

#                           EXERCICIO 21
#~~~~~~~~ colocar musica no codigo com o python


## pygame.init() ----- iniciando a função do pygame
## pygame.mixer.music.load('nomedoarquivo.mp3')          ---- a função escolhida do pygame dentro de diversas,
##                                                                        foi o MIXER.MUSIC

## pygame.mixer.mmusic.play()                           --- depois de fazer o load, só dar play
## pygame.event.wait()                          --- para esperar a musica acabar para assim encerrar o programa