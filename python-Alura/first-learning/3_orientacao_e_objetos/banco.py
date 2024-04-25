def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular':titular, 'saldo':saldo, 'limite':limite}
    return conta

conta = cria_conta(numero=123, titular='Leo', saldo=55.0, limite=1000.0)
print(conta['numero'])

def deposita(conta, valor):
    conta['saldo'] += valor
    
def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta['saldo']))