import pandas as pd

df4 = pd.DataFrame({'Nome': ['Cris', 'Jose', 'lais', 'Julia'],
                    'Idade':[24, 56, 56, 34]},
                    index=['Indice A', 'Indice B', 'Indice C', 'Indice D'])


# DEFININDO O NOME DO CAMPO INDICE 
print(df4.set_index("Nome", inplace=True))

