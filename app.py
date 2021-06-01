import traceback
from subtraction import Subtraction
from addition import Addition
from multiplication import Multiplication
from division import Division
from exceptions import CalculatorInputError

options = [
  '1: Addition',
  '2: Subtraction',
  '3: Multiplication',
  '4: Division'
  ]

def get_numbers():
  user_numbers_input = input('Enter the numbers you would like to use (seperate by spaces): ').split()
  try:
    for num in user_numbers_input:
      float(num) #float seems to work for int and float, so no need to check both.
  except ValueError:
    raise CalculatorInputError()
  except:
    traceback.print_exc()
  return user_numbers_input

print('Welcome to the simple calculator, please chose one of the following options: ')
for option in options:
  print(option)

def start_calc():
  user_selection = 0
  try:
    user_selection = int(input('Enter Your Selection: '))
  except ValueError:
    print('Error: Your input is not a number')
  except:
    traceback.print_exc()

  if(user_selection == 1 or 2 or 3 or 4):
    if(user_selection == 1):
      Addition(get_numbers())
    elif(user_selection == 2):
      Subtraction(get_numbers())
    elif(user_selection == 3):
      Multiplication(get_numbers())
    elif(user_selection == 4):
      Division(get_numbers())
    else:
      print('Error: Make a valid selection, 1-4')
      start_calc()

start_calc()