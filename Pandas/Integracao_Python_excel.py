'''
PANDAS:
 MAIS USADA NO GERAL
 TRATA O EXCEL COMO UMA BASE DE DADOS
 FAZ O QUE QUISER COM O ARQUIVO 
 PODE DESFAZER A ESTRUTURA ORIGINAL DO ARQUIVO CASO QUEIRA EDITAR

 OPENPYXL
 TRATA O EXCEL COMO UMA PLANILHA MESMO QUE POSSA TER VARIAS COISAS
 EDITA "COMO SE FOSSE UM VBA"
 MENOS EFICIENTE 
 MANTEM A ESTRUTURA ORIGINAL DO ARQUIVO, MAS CUIDADO PORQUE NAO NECESSARIAMENTE TUDO, TEM QUE TESTAR

'''

import pandas as pd
from openpyxl import workbook, load_workbook
tabela = pd.read_excel("Produtos.xlsx")

#PANDAS 
#atualizar o multiplicador 
tabela.loc[tabela["Tipo"]=="Serviço","Multiplicador Imposto"] = 1.5


# fazer a conta do preço base reais 
tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]
#print(tabela)

tabela.to_excel("ProdutosPandas.xlsx", index = False)

#OPENPYXL
planilha = load_workbook("Produtos.xlsx")
aba_ativa = planilha.active

for celula in aba_ativa["C"]:
    if celula.value == "Serviço":
        linha = celula.row
        aba_ativa[f"D{linha}"] = 1.5  

planilha.save("ProdutosOpenPy.xlsx")