import pandas as pd
dados = {
    "cargos": ["assistente", "analista", "gerente", "diretor"],
    "salarios" : [1000, 2000, 3000, 4000],
     
}
dados_bi= pd.DataFrame(dados)
#print(dados_bi) imprime todos os dados
#print(dados_bi.head(2)) imprime as duas primeiras 
#print(dados_bi.tail(2)) imprime as duas ultimas
#print(dados_bi[2:4]) imprime o intervalo
#print(dados_bi.shape) imprime linhas e colunas existentes
#exportando para CSV
dados_bi.to_csv("meus dados.csv", index=False, sep=";", encoding="utf-8")
print("Arquivo exportado com sucesso!")
