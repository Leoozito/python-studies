kmDaViagem = int(input("As kilometragens da sua viagem: "))
preco200km = kmDaViagem * 0.50
precoMaisKm = kmDaViagem * 0.45

if kmDaViagem > 200:
    print("Sua viagem ficara no valor de: {:.2f} reais".format(precoMaisKm))
else: 
    print("Sua viagem ficara no valor de: {:.2f} reais".format(preco200km))