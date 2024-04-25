#                   EXERCICIO 29 

velocidade = int(input("Velocidade percorrida: "))
multa = 7.0 
parteDaMulta = velocidade - 80
totalDaMulta = parteDaMulta * 7

print(f"Você passou do permitido, sua velocidade foi de [ {velocidade}km ], ou seja, você atingiu [ {parteDaMulta}km ] a mais de km, portanto sua multa será [ {totalDaMulta} reais]" if velocidade > 80 else "Prossiga, dirigindo com cuidado")
