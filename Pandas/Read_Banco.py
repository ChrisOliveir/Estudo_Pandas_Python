import pandas as pd
import pyodbc
from openpyxl import Workbook
dados_conexao = ("Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-TEO5HBQ\SQLEXPRESS;Database=AdventureWorks;Trusted_connection=yes")

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("SELECT [Name] FROM [AdventureWorks].[HumanResources].[Department]")

valores = cursor.fetchall()

tabela_valores = pd.DataFrame.from_records(valores)


wb = Workbook()
ws = wb.active
ws.cell(1, 1, "CARGO")
wb.save('C:/Users/Chris/OneDrive/tabela_valores.xlsx')



#print(tabela_valores)

