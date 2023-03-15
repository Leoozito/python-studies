# #               EXERCICIO 05 -----------
numero = int(input("Digite seu número favorito: "))
antecessor = numero - 1 
sucessor = numero + 1
print("\n[  SOBRE SEU NUMERO  ]\n")
print(f"seu numero [ {numero} ] tem como seu antecessor o {antecessor}, e seu sucessor o {sucessor}\n")

# #               EXERCICIO 06
resultadoDobro = numero * 2
resultadoTriplo = numero * 3
resultadoRaizQua = numero**(1/2)

print(f"O dobro do numero que você digitou é {resultadoDobro}")
print(f"O triplo do numero que você digitou é {resultadoTriplo}")
print(f"A raiz quadrada do numero que você digitou é {resultadoRaizQua}") 
print("A raiz quadrada do numero que você digitou é {:.2f}".format(resultadoRaizQua)) 
print("----------------------------------------------------------------------------")

# #               EXERCICIO 07
print("ESCOLA \n")

bimestre1 = float(input("Insira nota do 1° Bimestre : "))
bimestre2 = float(input("Insira nota do 2° Bimestre : "))
bimestre3 = float(input("Insira nota do 3° Bimestre : "))
bimestre4 = float(input("Insira nota do 4° Bimestre : "))

notaFinal = (bimestre1 + bimestre2 + bimestre3 + bimestre4) / 4
print(f"\n sua média final é: {notaFinal}")
print("----------------------------------------------------------------------------")
# #               EXERCICIO 08
metros = int(input("De quantos METROS você quer fazer conversões? \n"))

decimetro = metros * 10
centimetro = metros * 100
milimetro = metros * 1000
print(f"\n {metros} metro(s), tem {centimetro} centimentros \n {milimetro} milimetros \n {decimetro} decimetros")
print("----------------------------------------------------------------------------")

# #               EXERCICIO 09 
numeroDesejado = int(input("Insira o numero que você gostaria de ver a tabuada? "))
print("\n {} x {} = {}".format(numeroDesejado, 1 , numeroDesejado* 1))
print("\n{} x {} = {}".format(numeroDesejado, 2 , numeroDesejado* 2))
print("\n{} x {} = {}".format(numeroDesejado, 3 , numeroDesejado* 3))
print("\n{} x {} = {}".format(numeroDesejado, 4 , numeroDesejado* 4))
print("\n{} x {} = {}".format(numeroDesejado, 5 , numeroDesejado* 5))
print("\n{} x {} = {}".format(numeroDesejado, 6 , numeroDesejado* 6))
print("\n{} x {} = {}".format(numeroDesejado, 7 , numeroDesejado* 7))
print("\n{} x {} = {}".format(numeroDesejado, 8 , numeroDesejado* 8))
print("\n{} x {} = {}".format(numeroDesejado, 9 , numeroDesejado* 9))
print("\n{} x {} = {}".format(numeroDesejado, 10 , numeroDesejado* 10))
