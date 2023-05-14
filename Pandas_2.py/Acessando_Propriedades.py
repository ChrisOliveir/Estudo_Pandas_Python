import pandas as pd

df4 = pd.DataFrame({'Nome': ['Cris', 'Jose', 'lais', 'Julia'],
                    'Idade':[24, 56, 56, 34]},
                    index=['Indice A', 'Indice B', 'Indice C', 'Indice D'])

#PODEMOS ACESSAR A PROPRIEDADE DE UM OBJETO:
#print(df4['Nome'])
#OU
#print(df4.Nome)
#OU
#print(df4['Nome'][0]) # --> acessa o primeiro elemento da coluna nome

#PARA SELECIONAR A PRIMIERA LINHA DE DADOS EM UM DF PODEMOS USAR:
#print(df4.iloc[0]) 

# PARA SELECIONAR TODAS AS LINHAS E A PRIMEIRA COLUNA
#print(df4.iloc[:, 0])

#PARA SELECIONAR SEGUNDA E TERCEIRA LINHA DA PRIMEIRA COLUNA
#print(df4.iloc[1:3, 0]) # não pega o primeiro elemento da lista.


#Podemos usar numerops negativos na seleção 
print(df4.iloc[-3]) # pega o terceiro de trás para frente.
print(df4.iloc[-2:]) # pega as duas últimas linhas.

#SELEÇÃO BASEADA EM RÓTULOS
print(df4.loc['Indice A', 'Nome']) #Pega o nome do indice A
print(df4.loc[:,'Nome']) # pega todos os nomes da coluna NOME