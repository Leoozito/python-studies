# USANDO O FOR RANGE

def odd_or_even():
    soma_impares = 0
    for i in range(1, 11, 2):
        soma_impares += i
    print(soma_impares)

def descrescent_number():
    for i in range(10, 0, -1):
        print(i)