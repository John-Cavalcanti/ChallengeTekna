# my imports
import auxiliar.aux_functions as aux

# third party imports
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

aux.loading_screen()

# global
first_iteration = True
situacao_column_string = "Situação"
nota_para_aprovacao_column_string = "Nota para Aprovação Final"
sheet_name = "Software Engineer - Challenge [João Cavalcanti]"

scopes = ['https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(
  'TeknaChallenge-chave.json', scopes=scopes
)
client = gspread.authorize(credentials)

def get_sheet_data():
  sheet = client.open('Software Engineer - Challenge [João Cavalcanti]').sheet1
  data = sheet.get_all_values()
  return sheet, data

aux.clear_screen()

while True:
  if first_iteration:
    aux.greetings_text()
    first_iteration = False
  else:
    aux.another_choice()
  
  option = aux.select_menu()
  
  if option == "3":
    aux.clear_screen()
    break
  
  print("Check the sheet for updates...")
  
  # getting the sheet reference and their data
  sheet, data = get_sheet_data()
  df = pd.DataFrame(data)

  # defining columns and their content
  df.columns = df.iloc[2]
  df = df.iloc[3:]
  
  if option == "1":
    # converting columns content to numeric and calculating the situation
    df[["Faltas","P1","P2","P3"]] = df[["Faltas","P1","P2","P3"]].apply(pd.to_numeric)
    df[[situacao_column_string,nota_para_aprovacao_column_string]] = df.apply(aux.calculate_situacao_and_nota, axis=1, result_type='expand')
  elif option == "2":
    df[[situacao_column_string,nota_para_aprovacao_column_string]] = ""
  
  # preparing the values to update the sheet
  situations = df[situacao_column_string].tolist()
  final_grade_for_approval = df[nota_para_aprovacao_column_string].tolist()

  # update the sheet
  sheet.update(range_name=f"G4:G{len(situations) + 3}", values=[[s] for s in situations])
  sheet.update(range_name=f"H4:H{len(final_grade_for_approval) + 3}", values=[[n] for n in final_grade_for_approval])
  aux.clear_screen()
  
