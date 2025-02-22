import gspread
import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

maximum_absences = 15

# functions
def calculate_situacao_and_nota(row):
  average = (row['P1'] + row['P2'] + row['P3']) / 3
  
  if row['Faltas'] > maximum_absences:
    return "Reprovado", 0
  elif average >= 70:
    return "Aprovado", 0
  elif average < 50:
    return "Reprovado", 0
  else:
    final_grade_for_approval = 100 - average
    return "Recuperação", round(final_grade_for_approval)
  
  

scopes = ['https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(
  'TeknaChallenge-chave.json', scopes=scopes
)

client = gspread.authorize(credentials)
sheet = client.open('Software Engineer - Challenge [João Cavalcanti]').sheet1

dados = sheet.get_all_values()

df = pd.DataFrame(dados)

# defining columns and their content
df.columns = df.iloc[2]
df = df.iloc[3:]

# converting columns content to numeric
df[["Faltas","P1","P2","P3"]] = df[["Faltas","P1","P2","P3"]].apply(pd.to_numeric)
df[["Situação","Nota para Aprovação Final"]] = df.apply(calculate_situacao_and_nota, axis=1, result_type='expand')

print(df)
