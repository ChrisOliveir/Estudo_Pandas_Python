import pandas as pd
import pyodbc

dados_conexao = ("Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-TEO5HBQ\SQLEXPRESS;Database=AdventureWorks;Trusted_connection=yes")

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute(''' DELETE FROM HumanResources.Department WHERE DepartmentID=17 ''')

cursor.commit()

cursor.close()
conexao.close()

print("ok")


