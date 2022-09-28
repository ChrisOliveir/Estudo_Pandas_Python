import pandas as pd 

'''As vezes precisaremos mudar o encoding. Possiveis valores para testar:
encoding= 'Latin1, encoding='ISO-8859-1 ,encoding='utf-8', ou entao encoding='cp1252'
'''

vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

'''print(vendas_df)
print(produtos_df)
print(lojas_df)
print(clientes_df)'''

# TIRANDO COLUNAS INÚTEIS DO CLIENTE_DF 

clientes_df = clientes_df.drop(['Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10'], axis=1) # tira tando linha como 
# colunas, se eu nao passar nada ele tira as linhas, entao eu forneço "axis=1" que representa o eixo colunas

# ESCOLHENDO COLUNAS QUE QUERO PEGAR 

clientes_df = clientes_df[['ID Cliente','E-mail']]
produtos_df= produtos_df[['ID Produto','Nome do Produto']]
lojas_df = lojas_df[['ID Loja','Nome da Loja']]

#JUNTANDO OS DATAFRAMES PARA TER 1 SÓ 

vendas_df = vendas_df.merge(produtos_df, on="ID Produto")
vendas_df = vendas_df.merge(lojas_df, on="ID Loja")
vendas_df = vendas_df.merge(clientes_df, on="ID Cliente")


# MUDANDO NOME DE COLUNA 
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})
print(vendas_df)

