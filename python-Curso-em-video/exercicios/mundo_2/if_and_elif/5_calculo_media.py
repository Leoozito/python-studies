nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

mediafinal = (nota1 + nota2) / 2

print(f"Com o aluno tirando {nota1} e {nota2} sua media é de {mediafinal}, sendo assim")

if mediafinal > 6:
   print("O aluno está APROVADO")
elif mediafinal > 4 and mediafinal < 6:
    print("O aluno está RECUPERAÇÃO")
else:
    print("O aluno está REPROVADO")