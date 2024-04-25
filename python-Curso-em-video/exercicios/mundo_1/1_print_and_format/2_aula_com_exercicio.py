# Exercicio de tipagem , juntamente com a função IS (função booleana)

#                           EXERCICIO 04

n = input("Digite qualquer coisa: ")

print("A tipagem da variavel N é", type(n))
print("-----------------------------------------")
print("Só tem espaços?", n.isspace())
print("É um numero", n.isnumeric())
print("É um alfabético", n.isalpha())
print("É um alfanúmerco", n.isalnum())
print("Está em minusculo", n.islower())
print("Está em maiuscula", n.isupper())
print("Esta capitalizada?", n.istitle()) # capitalizada : com letra maiuscula e minuscula