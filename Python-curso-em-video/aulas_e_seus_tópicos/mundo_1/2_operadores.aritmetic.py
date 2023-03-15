# " ** " Significa potência
# " // " divisão inteira
# " % " resto da divisão

valor1 = int(input("seu PRIMEIRO número: "))
valor2 = int(input("seu SEGUNDO número: "))
print("---------------------------------------------")
# Potencia
resultadoPotencia = valor1 ** valor2
resultadoPotencia2 = pow(valor1, valor2) 

# Divisão inteira
resultadoDivInt = valor1 // valor2

# Resto da divisão 
resultadoRestoDiv = valor1 % valor2

print(f"Resultado da potencia é {resultadoPotencia}, e por meio de OUTRO JEITO de fazer a conta de potencia, também da o resultado {resultadoPotencia2}")
print(f"Resultado da divisão inteira é {resultadoDivInt}")
print(f"Resto da divisão é {resultadoRestoDiv}")

## ORDEM DE PRECEDENCIA : 1° Nas operações só se usa o parenteses, e o ' () ' é o primeiro a ser executado. 
# 2° ' ** ' potencia. 
# 3° " * , / , // , %". 
# 4° " + e - ".  

## Calcular RAIZ QUADRADA 
resultadoRaizQua = valor1**(1/2)
resultadoRaizCubica = valor1**(1/3)

print(f"A raiz quadrada de {valor1} é {resultadoRaizQua}")
print(f"A raiz cubica de {valor1} é {resultadoRaizCubica}")
print("-------------------------------------------------------")

## Para juntar os print na mesma linha usando END.
print("Eu sou o", end='') 
print(" Leonardo Nogueira")
# Para quebrar linha 
print("\n Eu \n sempre \n serei \n O MELHOR") 