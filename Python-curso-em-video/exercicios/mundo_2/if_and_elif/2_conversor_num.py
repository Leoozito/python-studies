numero = int(input("Para começarmos, digite um número: "))

print("Escolha uma das bases para conversão: ")
print("[ 1 ] converter para BINARIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")

opcao = int(input("Sua opção: "))

if opcao == 1:
    binario = bin(numero)
    print(f"O número [ {numero} ] que você digitou, o formato dele em BINARIO é: [ {binario[2:]} ]")
elif opcao == 2:
    octal = oct(numero)
    print(f"O número [ {numero} ] que você digitou, o formato dele em OCTAL é: [ {octal[2:]} ]")
elif opcao == 3:
    hexa = hex(numero)
    print(f"O número [ {numero} ] que você digitou, o formato dele em HEXADECIMAL é: [ {hexa[2:]} ]")
else:
    print("-="*20)
    print("Opção que você digitou invalida.")

