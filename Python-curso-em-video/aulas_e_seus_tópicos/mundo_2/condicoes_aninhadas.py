# aninhar é como se fosse colocar uma coisa dentro da outra, encaixando as coisas.
# é ensinado sobre o uso de ELIF

# se diz condição aninhada pelo fato de haver uma coisa dentro da outra, tipo um ninho, ou seja, elif's dentro de if's 

nome = str(input("Qual é o seu nome?"))

if nome == "Leonardo": 
    print(f"Nome lindo! Bom dia {nome}")
elif nome == "Yasmin":
    print(f"Nome legal! Bom dia {nome}")
    #atenção no uso de OR
elif nome == "Pedro" or nome == "João" or nome == "Maria":
    ("Seu nome é bem popular no Brasil")
    # atenção no uso do IN
elif nome in 'Ana Claudia Jessica Juliana':
    print("Belissimo nome feminino")
else:
    print(f"Bom dia {nome}")