class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return f"Codigo: {self.codigo} Saldo {self.saldo}"
    
conta_Leozito = ContaCorrente(123)
print(conta_Leozito)
# para mudar o saldo
conta_Leozito.deposita(3000000.0)
print(conta_Leozito)
