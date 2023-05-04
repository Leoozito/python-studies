""" tipos de triangulos: Equilatero Isósceles e Escaleno """

lado_1 = float(input("Primeiro segmento: "))
lado_2 = float(input("Segundo segmento: "))
lado_3 = float(input("Terceiro segmento: "))

if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2:
    print('Os segmentos acima PODEM FORMAR um triangulo!')
    if lado_1 == lado_2 == lado_3:
        print("Com essas medidas conseguimos formar um triangulo EQUILÁTERO")
    elif lado_1 != lado_2 != lado_3 != lado_1:
        print("Com essas medidas conseguimos formar um triangulo ESCALENO")
    else: 
        print("Com essas medidas conseguimos formar um triangulo ISÓSCELES")
else:
    print('Os segmentos acima NÃO PODEM FORMAR triangulo')