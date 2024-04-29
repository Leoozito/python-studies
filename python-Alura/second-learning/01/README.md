### Codigos especificos ensinados

> Formatações no print
```py
print(f'O valor arredondado de pi é: {pi:.2f}')
print('A','L','U','R','A',sep='\n')
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
> Lista e Tupla
-   As **listas** são ideais quando você precisa de uma coleção de elementos que pode ser modificada **ao longo do tempo**. Lista é multável

-   As **tuplas** têm um desempenho melhor do que listas para algumas operações. Elas são mais eficientes em **termos de espaço e processamento** em determinados cenários. Ás tuplas são imutáveis