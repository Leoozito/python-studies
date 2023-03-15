#           IF AND ELSE

nome = str(input("Qual é seu nome?: "))
if nome == 'Leonardo':
    print("Que nome lindo você tem")
else:
    print("Olá")
print(f"Bom dia {nome}")
print("------------------------------------------------")

nota1 = float(input("Digite sua 1° nota: "))
nota2 = float(input("Digite sua 2° nota: "))
media = (nota1 + nota2) / 2

# Condição composta
# if media >= 6:
#     print("PARABENS, voce foi aprovado")
# else:
#     print("Você foi reprovado")
    
#Condição simplificada
print(f"Sua média foi: {media}")
print("Parabéns !!!" if media > 6 else "Reprovado!")