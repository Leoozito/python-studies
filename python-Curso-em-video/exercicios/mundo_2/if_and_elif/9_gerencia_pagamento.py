preco_total = float(input("Valor total da compra: "))
print("[1] à Vista\n[2] à Vista no Cartão\n[3] 2x no cartão\n[4] 3x á 12x sem juros")
forma_pagamento = int(input("Informe sua forma de pagamento: "))

a_vista = preco_total - (preco_total  * 10 / 100)
a_vista_cartao = preco_total - (preco_total * 5 / 100)
x2_cartao = preco_total / 2
juros = preco_total - (preco_total * 20 / 100)

if (forma_pagamento == 1):
    print(f"Valor da sua compra: {preco_total}\nDesconto de: 10%\nValor á pagar: {a_vista}")
elif (forma_pagamento == 2):
    print(f"Valor da sua compra: {preco_total}\nDesconto de: 5%\nValor á pagar: {a_vista_cartao}")
elif (forma_pagamento == 2):
    print(f"Valor da sua compra: {preco_total}\nParcela: 2x de {x2_cartao}%\nValor á pagar: {a_vista}")
else:
    parcela = float(input("Você escolheu dividir de 3x á 12x, informe exatamente a quantidade do parcelamento desejado"))
    
    maisx_cartao = (preco_total + juros) / parcela
    valor_cada_parcela = preco_total / parcela

    print(f"Valor da sua compra: {preco_total}\nParcela: {parcela}x de {valor_cada_parcela}%\nJuros:{juros}\nValor á pagar: {a_vista}")
     