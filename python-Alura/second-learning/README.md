# Sumário das pastas

## Pasta 01 - 1° Parte do curso -> "Python: Crie a sua primeira aplicação": 

Descrição de topicos ensinados no curso
-   Print e Input para armazenar valor 
-   Variaveis 
-   If Else, Match 
-   **Funções**, Utilização da função MAIN
-   **Bibliotecas:** Para dar um delay de segundos | Para limpar o terminal

Formatações no **print**
```py
print(f'O valor arredondado de pi é: {pi:.2f}')
print('A','L','U','R','A',sep='\n')
```

#### Instrução MATCH

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