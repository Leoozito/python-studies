# Quando atribuimos alguma frase a uma variavel, o Python por trás , guarda na memoria do computador, e pra isso ele cria mini's espaços para cada letra e espaço dessa frase.

# Operações para fatiar strings - explicação no caderno -
# Analise de strings  - explicação no caderno - 
# Transformação - explicação no caderno -

#                                         FATIAÇÃO DE FRASES

frase = "Curso em Video Python"
print("1°: ",frase[3:13])
print("2°: ",frase[:13])

print('\n3°: ',frase[1:15:2]) #     O ultimo PULANDO de dois em dois 
print("4°: ",frase[::2])
# QUANTAS vezes da tal palavra especificada tem 
print('\n5°: ',frase.upper().count('O'))
# TAMANHO da frase
print("6°: ",len(frase))
# para TROCAR palavras especifica por outra em uma só instancia
print('\n7°: ',frase.replace('Python', 'Android'))
print("8°: ",frase)
# para ENCONTRAR a posição onde a palavra se encontra
print("9°: ",frase.find('Video'))

dividido = frase.split() # transforma em uma LISTA

# possibilitando até ACESSAR e pegar palavras especifica
print("\n10°: ", dividido[0]) 
# ou pegar uma LETRA especifica ("vai até a palavra da posição * 3 * e trás a letra da posição * 0 * ")
print("11°: ",dividido[3][0]) 
print("-------------------------------------------------------------------------------\n")

## três aspas para colocar um texto com paragrafos, quebras de linhas
print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book.""") 
print("-------------------------------------------------------------------------------")
