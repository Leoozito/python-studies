from conta import ContaCorrente

# definindo perfil de conta por meio do objeto e colocando na memoria desse objeto criado no meio classe no arquivo "conta" -> EXECUÇÃO QUE GUARDA PRA MEMÓRIA
conta1 = ContaCorrente(1234, "Vitoria Regia", 25550.0, 1000000000.0)
conta2 = ContaCorrente(12345, "Leozito", 130000.0, 600000000000.0)
conta3 = ContaCorrente(123, "Yasmin", 7320.0, 7000000.0)
# estrutura para printar partes definidas
# print(conta3.saldo)

conta3.extrato()
conta3.deposita(60000.0)
conta3.extrato()

conta3.saca(60000.0)
conta3.extrato()

print("-=-"* 15)
conta2.transfere(10000.0, conta3)
conta2.extrato()
conta3.extrato()
# chamando um metodo estatico

codigo = ContaCorrente.codigos_bancos()
print(codigo)

