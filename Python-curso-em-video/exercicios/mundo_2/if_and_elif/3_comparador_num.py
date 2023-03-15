primeirovalor = int(input("Digite o primeiro valor: "))
segundovalor = int(input("Digite o segundo valor: "))

if primeirovalor > segundovalor:
    print(f"O primeiro valor é maior")
elif segundovalor < primeirovalor:
    print(f"O segundo valor é maior")
else:
    print("Não existe maior, os dois são iguais")