ano_de_nascimento = int(input("Ano de nascimento é: "))
calcula_idade = 2023 - ano_de_nascimento

print(f"Quem nasceu em {ano_de_nascimento} tem {calcula_idade} anos de idade em 2023")
if calcula_idade < 18:
    anos_que_faltam =  18 - calcula_idade
    ano_do_alistamento = anos_que_faltam + 2023
    print(f"Ainda falta {anos_que_faltam} anos para seu alistamento")
    print(f"Seu alistamento será em {ano_do_alistamento}")
elif calcula_idade > 18:
    ano_que_passaram = 2023 - ano_de_nascimento
    ano_que_ja_passaram -= 18
    ano_do_alistamento = 2023 - ano_que_ja_passaram
    print(f"Você ja deveria ter se alistado á {ano_que_ja_passaram} anos")
    print(f"Seu alistamento era pra ter sido feito em {ano_do_alistamento}")
else:
    print("ALISTADO")