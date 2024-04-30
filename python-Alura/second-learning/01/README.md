### Codigos especificos ensinados

> Formatações no PRINT

```py
print(f'O valor arredondado de pi é: {pi:.2f}')
print('A','L','U','R','A',sep='\n')
print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') # o ljust serve para dar ESPAÇAMENTO
```

> Instrução MATCH

```py
opcao_escolhida = int(input('Escolha uma opção: '))
match opcao_escolhida:
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case _:
        print('Opção inválida!')
```

> DICIONARIOS , LISTA E TUPLA

```py
lista = [1,’olá mundo’,True,9.7]
tupla = (1,’olá mundo’,True,9.7)

# acesso dicionario
dicionario = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True}]

for restaurante in dicionario:
    nome_restaurante = restaurante['nome']
    print(f' - {nome_restaurante}')

```

-   Os **DICIONARIOS** são "mais importante", pelo fato de dividir grupos com seus devidos dados 

-   As **LISTAS** são ideais quando você precisa de uma coleção de elementos que pode ser modificada **ao longo do tempo**. Lista é multável

-   As **TUPLAS** têm um desempenho melhor do que listas para algumas operações. Elas são mais eficientes em **termos de espaço e processamento** em determinados cenários. Ás tuplas são imutáveis

> FOR e WHILE

```py
for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break
print("Você digitou:", numero)
```

-   **FOR** é utilizado quando se conhece previamente o número de iterações que devem ser realizadas.

-   **WHILE** é utilizado quando o número de iterações não é conhecido de antemão

```py
numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)
```

> Operador ternário

```py
exemplo = True
ativo = 'ativado' if exemplo else 'desativado'
print(ativo) # 'ativado'
```