import pandas as pd 

vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
#print(vendas_df[:3]) pega ate a linha de indice 43 do dataframe

#print(vendas_df[['Numero da Venda', 'Data da Venda', 'ID Produto']]) --> cria um dataframe com as colunas x, y...

#print(vendas_df['ID Produto'][0])  pega o item da 1 linha da coluna x

#print(vendas_df.info())  informações sobre a base que estou importando

#lista_clientes = vendas_df['ID Cliente']
#print(lista_clientes)

produtos_quantidade = vendas_df[['ID Produto', 'Quantidade Vendida','Quantidade Devolvida']]
print(produtos_quantidade)