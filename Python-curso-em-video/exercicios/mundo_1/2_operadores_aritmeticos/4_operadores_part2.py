
# #               EXERCICIO 10
reaisBRL = float(input("Insira o valor exato de reais que você possui: "))
dolarUSD = reaisBRL / 5.41

print("A conversão de seus reais para dolar é: {:.2f}".format(dolarUSD))
print("----------------------------------------------------------------------------")

# #               EXERCICIO 11 
largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))

metrosArea = largura * altura
print(f"\n Sua parede tem dimensão {largura} x {altura} e sua área é de {metrosArea} quadrados")
tinta = metrosArea / 2
print(f"Então você precisará de {tinta} litros de tinta\n")
print("----------------------------------------------------------------------------")

#               EXERCICIO 12 
preco = float(input("O preço do produto é: "))
desconto = (5 / 100) * preco
precoComDesconto = preco - desconto 
print(f"O valor com desconto de 5% ficará {precoComDesconto}")
print("----------------------------------------------------------------------------")

#               EXERCICIO 13
salario = float(input("Seu sálario é: "))
aumento = (15 / 100 ) * salario
salarioComAumento = salario + aumento 
print("Seu salario com aumento ficou: {:.2f}".format(salarioComAumento))