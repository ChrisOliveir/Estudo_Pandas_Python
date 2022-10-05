import pandas as pd
import sqlite3
import pyodbc

'''conexao = sqlite3.connect('salarios.sqlite')
tabela_salarios = pd.read_sql('SELECT * FROM Salaries',conexao)

conexao.close()

print(tabela_salarios)'''

#print(pyodbc.drivers())

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=salarios.sqlite")
conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute('SELECT * FROM Salaries')
 # quando usamos o pyodbc os nomes das colunas e valores ficam separadas
valores = cursor.fetchall() # valores onde é uma lista de tuplas, onde cada tupla é uma linha da tabela [()]
descricao = cursor.description #colunas

colunas = [tupla[0] for tupla in descricao] # as colunas vao ser uma lista onde o primeiro item da tupla [tupla[0]] para cada tupla que esta dentro da descição

tabela_salarios2 = pd.DataFrame.from_records(valores, columns=colunas)
print(tabela_salarios2)
