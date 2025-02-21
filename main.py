import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

scopes = ['https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(
  'TeknaChallenge-chave.json', scopes=scopes
)

client = gspread.authorize(credentials)
sheet = client.open('Software Engineer - Challenge [João Cavalcanti]').sheet1

print(sheet.get_all_values())
