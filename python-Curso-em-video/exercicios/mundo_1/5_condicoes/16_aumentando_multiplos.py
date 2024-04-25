salario = int(input("Quanto você recebe de salário: "))
part10porcento = salario * 10 / 100
part15porcento = salario * 15 / 100  

salario10Aumento = salario + part10porcento
salario15Aumento = salario + part15porcento

if salario >= 1250:
    print(f"Seu salario de {salario} reais, aumentará para {salario10Aumento} reais")
else:
    print(f"Seu salario de {salario} reais, aumentará para {salario15Aumento} reais")

