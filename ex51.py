import pandas as pd
df=pd.read_csv('ClassicDisco.csv')
#imprime todos os dados da planelha print(df.to_string())
#exibe as 5 primeiras linhas
#print(df.head())
#exibe as 5 ultimas linhas
#print(df.tail(9))
#intervalo entre linhas
#print(df[10:15])
#mostra o numero de linhas e colunas
print(df.shape)
