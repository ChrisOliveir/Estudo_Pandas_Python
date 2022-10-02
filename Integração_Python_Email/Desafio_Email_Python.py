import pandas as pd
import win32com.client as win32

gerentes_df = pd.read_excel("Enviar email.xlsx")

for i in enumerate (gerentes_df['E-mail']):
    gerente = gerentes_df.loc[i, 'gerente'] #loc filtra linhas 
    area = gerentes_df.loc[i, 'Relatorio']

   
