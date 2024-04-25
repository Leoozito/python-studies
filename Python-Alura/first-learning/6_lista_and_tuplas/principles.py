# Para fazer listas novas e interativas 
idades = []

idades.extend([19,23,56,78,9,0])

idades_no_ano_que_vem = [(idades+1) for idades in idades]
idades_no_ano_passado = [(idades-1) for idades in idades]
print(idades_no_ano_passado ,"\n", idades, "\n", idades_no_ano_que_vem)

maior_de_18 = [(idades) for idades in idades if idades > 18]
print("\n",maior_de_18)
print("-" * 30)
print("TUPLAS \n")

leozito = ("Leonardo", 20, 2002)
vitoria = ("Vitoria", 15, 2008)
#usando tuplas dentro de uma lista mutavel, seguindo a logica de que, os dados dos usuarios não podem mudar, mas pode ser adicionado mais usuarios para a lista.
usuarios = [leozito, vitoria]
print(usuarios)

#ARRAY
