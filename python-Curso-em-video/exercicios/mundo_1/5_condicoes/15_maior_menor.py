# Feito pelo professor
# Não esquecer do AND 

a = int(input("Digite seu 1° numero: "))
b = int(input("Digite seu 2° numero: "))
c = int(input("Digite seu 3° numero: "))

menor = a 
#Verificando quem é o menor
if b < a and b < c:
    menor = b 
if c < a and c < a:
    menor = c
# Verificando quem é o maior
maior = a

if b > a and b > c:
    maior = b
if c > a and c > b: 
    maior = c
    
print("----------------------------------------")
print(f"O maior valor digitado foi {maior}")
print(f"O menor valor digitado foi {menor}")
print("----------------------------------------")