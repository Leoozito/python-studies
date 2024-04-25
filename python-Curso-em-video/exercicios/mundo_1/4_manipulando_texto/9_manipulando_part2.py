#                        EXERCICIO 25 ------------
nome = str(input("Digite seu nome: ")).strip()
print("Seu nome tem Silva? {}".format('SILVA' in nome.upper())) # o in serve para ver o que tem dentro da variavel

#                       EXERCICIO 26 ------------
frase = str(input("Escreva algo: ")).strip()
print(frase.upper().count('A'), "° vezes aparece a letra A")
print(frase.upper().find('A')+1, "° é a posição da primeira letra A da frase") 
# é colocado o + 1 para as posições não começarem do 0 
print(frase.upper().rfind('A')+1, "° é a posição que a ultima letra A, está posicionada na sua frase") 
# rfind para o programa ler do lado direito e achar a ultima palavra

#                       EXERCICIO 27
digitaNome = str(input("Digite seu nome completo: "))
posicaoNome = digitaNome.split()

print(f"Seu primeiro nome é {(posicaoNome[0])}")
print(f"Seu ultimo nome é {(posicaoNome[-1])}")
