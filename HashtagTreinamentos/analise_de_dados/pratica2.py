# Passo a Passo
# Passo 1: Importa o BD para analisarmos
import pandas as pd
import plotly.express as px

tabela = pd.read_csv(r"C:\Users\leozi\Downloads\clientes.csv", encoding="latin", sep=";")

# Passo 2: Visualizar o BD
    # Entender as informações que você tem disponível
    # Procurar erros no BD
print(tabela.info())
     
# Passo 3: Tratar os erros do BD
    # acertar informações que estão sendo reconhecidas de forma errada
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
    # corrigir informações vazias, deletando colunas inúteis
tabela = tabela.drop("Unnamed: 8", axis=1)
tabela.dropna()

for coluna in tabela.columns:
    # cria o grafico
    grafico = px.histogram(tabela, x="Origem", y="Nota (1-100)", histfunc="avg")
    # exibe o grafico
    grafico.show()

# Passo 4: Analise Inicial -> Entender as notas dos clientes
# Passo 5: Analise completa -> Entender como cada característica do cliente impacta na nota