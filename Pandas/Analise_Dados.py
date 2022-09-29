import pandas as pd 

vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

# ESCOLHENDO COLUNAS QUE QUERO PEGAR 

clientes_df = clientes_df[['ID Cliente','E-mail']]
produtos_df= produtos_df[['ID Produto','Nome do Produto']]
lojas_df = lojas_df[['ID Loja','Nome da Loja']]

#JUNTANDO OS DATAFRAMES PARA TER 1 SÓ 

vendas_df = vendas_df.merge(produtos_df, on="ID Produto")
vendas_df = vendas_df.merge(lojas_df, on="ID Loja")
vendas_df = vendas_df.merge(clientes_df, on="ID Cliente")

# QUAL CLIENTE QUE COMPROU MAIS VEZES?
#METODO .VALUE_COUNTS() para contar quantas vezes cada valor do dataframe aparece

frequencia_clientes = vendas_df['E-mail'].value_counts()
print(frequencia_clientes)

