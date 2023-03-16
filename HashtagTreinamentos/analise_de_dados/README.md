
# Códigos úteis para tratamento de dados
```cpp
tabela = tabela.drop("Unnamed: 8", "Idade", axis=1)
```
no parenteses você coloca 1° o que irá apagar da tabela, e o "axis" se receber 0 é linha e 1 é coluna

```cpp
errors="coerce"
```
o coerce força a erros virarem um número vazio, ou seja -> NaN

```cpp
tabela.dropna()
```
apaga linhas com informações vazias

## Para analisar os dados
> Mais uma biblioteca do python : plotly
para criar graficos

```cpp
import plotly.express as px

px.histogram(tabela, x="Origem", y="Nota (1-100)")
```
o histogram serve para mostrar como as informações estão distribuidas nas tabelas

```cpp
histfunc="avg"
```
o calculo que o histograma faz dos dados (o padrão dele é somar)

```cpp
nbins=5
```
nbins serve para definir a quantidade de agrupamento que será feita