#                   EXERCICIO 22

nome = str(input("Digite seu nome completo: ")) 

print("\nNome digitado:", nome,'\n')
print(nome.upper())
print(nome.lower())

tamanhoDoNome = ''.join(nome.split())
print('\nSeu nome completo tudo junto, tem',len(tamanhoDoNome),'letras')

lista = nome.split()
tamanhoPrimNome = lista[0]
print(lista[0], end='')
print(", seu primeiro nome tem", len(tamanhoPrimNome), "letras")
print("------------------------------------------------------------\n")
#                   EXERCICIO 23 -------------

numero = int(input("Digite qualquer número: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f"Seu numero é {numero}")
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")

#                   EXERCICIO 24 ------------
print("------------------------------------------------------------\n")
n = str(input("Digite o nome da cidade: ")).strip()
print(n[:5].upper() == "SANTO")

