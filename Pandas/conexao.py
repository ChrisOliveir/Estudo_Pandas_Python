'''from sys import displayhook
import pyodbc 
import numpy as np
import pandas as pd
from openpyxl.workbook import Workbook
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')

dados_conexao = ("Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-TEO5HBQ\SQLEXPRESS;Database=AdventureWorks;Trusted_connection=yes")
#print(pyodbc.drivers())

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

rows = cursor.execute("SELECT * FROM [AdventureWorks].[HumanResources].[Department]")
lista = []
lista1 =[]
for row in rows:
    lista.append(row[1])
    lista1.append(row[2])

    
df_lista = pd.DataFrame(lista,columns=['Nome departamento'])

df_lista1 = pd.DataFrame(lista1,columns=['Nome Grupo'])

tabela = pd.concat([df_lista,df_lista1], axis=1)

tabela.to_excel('tabela python.xlsx', sheet_name='sheet', index= False)

# INTEGRAÇÃO DO EMAIL COM  PYTHON 

mail = outlook.CreateItem(0)
mail.To = 'christianeolive@hotmail.com, cristiane.araujo@ferroport.com.br'
mail.Body = 'Teste de envio de e-mail atraves do código python'

attachment = r'C:\Users\Chris\OneDrive\Área de Trabalho\proj\tabela python.xlsx'
mail.Attachments.Add(attachment)
mail.Send()
print('ok')'''