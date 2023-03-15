#                              EXERCICIO 14
celsius = float(input("Informe a temperatura em °C: "))
fahrenheit = ((9*celsius) / 5) + 32
print(f"{celsius}°C celsius em fahrenheit é {fahrenheit}°F")
print("-------------------------------------------------------")
#                              EXERCICIO 15
print ("ALUGA CARROS")
usoKm = float(input("\nQuantos km rodados:"))
usoDia = float(input("Quantos dias de uso:"))

totalPagamento = (usoKm * 0.15) + (usoDia * 60.0)
print(f"O valor a ser pago é {totalPagamento}")