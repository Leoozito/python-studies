peso = float(input("Informe o seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / (altura * altura)
# IMC 18.5
if imc < 18.5:
    print("Você está em estágio de Magreza")
elif imc < 24.9: 
    print("Você está em estágio de Normal")
elif imc < 29.9: 
    print("Você está em estágio de Sobrepeso ")
elif imc < 34.9: 
    print("Você está em estágio de Obesidade ")
else: 
    print("Você está em estágio de Obesidade Morbida, cuidado!")

