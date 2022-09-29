import win32com.client as win32

outlook = win32.Dispatch('outlool.application') #instancia do outlook

mail = outlook.CreateItem(0)
mail.To = 'christianeolive@hotmail.com'
mail.Subject = "teste"
mail.Body = 'Texto do E-mail'

#anexos (pode colocar quantos quiser):
attachment = r'C:\Users\Chris\OneDrive\Área de Trabalho\PandasSql\Financeiro.xlsx'
mail.Attachments.Add(attachment)

mail.Send()
print("ok")