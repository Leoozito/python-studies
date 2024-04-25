import datetime # ensinado, para pegar a data atual

# Minha formula
anoAtual = int(input("Que ano você quer analisar, Coloque 0 para analisar o ano atual: "))

if anoAtual % 4 == 0: 
    print("Seu ano é BISSEXTO")
else:
    print("Seu ano tem 365 dias")    
print("==================================================\n")

# Formula do professor

## Tem excessões, ou seja, o ano pra ser bissexto, ele não pode ser multiplos de 100, e serem multiplos de 400
if ano == 0:
    ano = date.today().year  # para pegar a data atual e .só o ANO
if anoAtual % 4 == 0 and anoAtual % 100 != 0 or anoAtual % 400 == 0: 
    print("Seu ano é BISSEXTO")
else:
    print("Seu ano tem 365 dias")   