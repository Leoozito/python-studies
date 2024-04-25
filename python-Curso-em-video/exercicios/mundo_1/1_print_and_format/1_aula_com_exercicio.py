# Exercicios Mostrando como funciona o input e o print
# Funcionalidades do ex 1 e 2: Aparecer na tela o que for digitado no terminal por meio dos inputs
# Funcionalidades do ex. 3: Soma e concatenação , e como funciona os TIPOS PRIMITIVOS e MÉTODO FORMAT

###                     EXERCICIO 1
print('============ Hello , World ! ===================')

nome = input('Digite seu nome: ')

print('Seja bem-vindo', nome, ', muito bom vê-lo')
print('===============================================')

###                     EXERCICIO 2
diaQueNasceu = input('informe o [dia] que você nasceu: ')
mêsQueNasceu = input('informe o [mês] que você nasceu: ')
anoQueNasceu = input('informe o [ano] que você nasceu: ')

print('Você nasceu no dia',diaQueNasceu,"do mês de",mêsQueNasceu,"no ano de",anoQueNasceu)

###                  EXERCICIO 3
print('===============================================')
firstNum = input('digita o 1° número: ')
secondNum = input('digita o 2° número : ')

somaCompleta = firstNum + secondNum
print(f'digitos escolhidos CONCATENADOS {somaCompleta}')

print('===============================================')
firstNum = int(input('digita novamente 1 número que agora você deseja SOMAR: '))
secondNum = int(input('digita novamente 2 número que agora você deseja SOMAR: '))

somaCompleta = firstNum + secondNum

print(f'{firstNum} sendo somado com {secondNum}, o resultado é [ {somaCompleta} ]')