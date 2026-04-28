import pandas as pd
dados = {'Vendedor' : ['Naruto', 'Goku', 'Seya'],
         "Produtos": ["Geladeira", "fogão", "ar condionado"],
         "Valor vendido" : [3400, 750, 2650,]}
df=pd.DataFrame(dados)
print(df)