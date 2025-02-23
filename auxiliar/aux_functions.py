import os

maximum_absences = 15

# functions
def calculate_situacao_and_nota(row):
  average = (row['P1'] + row['P2'] + row['P3']) / 3
  
  if row['Faltas'] > maximum_absences:
    return "AbsentFailed for Absence", 0
  elif average >= 70:
    return "Approved", 0
  elif average < 50:
    return "Failed by Grade", 0
  else:
    final_grade_for_approval = 100 - average
    return "Final Test", round(final_grade_for_approval)
  

def select_menu():
  print("Select an option and press enter to confirm:")
  print("1 - Calculate the average and situation of the students")
  print("2 - Clean the sheet")
  print("3 - Exit the program")
  option = input("Option: ")
  return option
  
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def loading_screen():
  clear_screen()
  print("Loading the sheet...")

def greetings_text():
  print("Hello! This is the selection menu\n")

def another_choice():
  print("What else you want to do?\n")
