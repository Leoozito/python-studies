from datetime import date

ano_de_nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade_atual = ano_atual - ano_de_nascimento

print(f"O atleta tem {idade_atual} anos")

if idade_atual <= 9:
    print("Classificação: MIRIM")
elif idade_atual <= 14:
    print("Classificação: INFANTIL")
elif idade_atual <= 19:
    print("Classificação: JÚNIOR")
elif idade_atual <= 25:
    print("Classificação: SÊNIOR")
elif idade_atual > 25:
    print("Classificação: MASTER")
else:
    print("Confira o que você digitou!")
