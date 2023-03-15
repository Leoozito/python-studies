#                   EXERCICIO 36

valordacasa = float(input("Valor da casa: "))
salario_comprador = float(input("Salario do comprador: "))
anos_financiamento = int(input("Quantos anos de financiamento: "))
prestacao = valordacasa / (anos_financiamento * 12)
minimo = salario_comprador * 30 / 100

print("Para pagar uma casa de R${:.2f} em {} anos, a prestação ficará de R${:.2f}".format(valordacasa, anos_financiamento, prestacao))
 
print(minimo)
 
if minimo <= prestacao:
    print('Emprestimo negado')
else: 
    print('Emprestimo concedido')
# if anos_financiamento > 10 or anos_financiamento < 0:
#     print("Infelizmente esse prazo é muito longo de acordo com as regras do banco")
