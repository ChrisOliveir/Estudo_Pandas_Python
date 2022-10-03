import pandas
import pyodbc
dados_conexao = ("Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-TEO5HBQ\SQLEXPRESS;Database=AdventureWorks;Trusted_connection=yes")

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute(""" INSERT INTO HumanResources.Department (Name, GroupName)
VALUES ('Médico', 'Saúde')
""")
cursor.commit()
print("ok")

cursor.commit()
cursor.close() # para garntir que finalizou a conexao com o banco para ele nao ficar bloqueado por conta da conexao anterior
