import pandas as pd 

vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
print(vendas_df[:3])
