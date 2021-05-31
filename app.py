from addition import Addition

options = [
  '1: Addition',
  '2: Subtraction',
  '3: Multiplication',
  '4: Division'
  ]

def get_numbers():
    try:
      user_numbers_input = [int(i) for i in input('Enter the numbers you would like to use (seperate by spaces): ').split()]
    except ValueError:
      print('input must be numbers')
    print(user_numbers_input)

    return user_numbers_input

print('Welcome to the simple calculator, please chose one of the following options: ')
for option in options:
  print(option)

def start_calc():
  try:
    user_selection = int(input('Enter Your Selection: '))
  except ValueError:
    print('Error: Your input is not a number')
  if(user_selection == 1 or 2 or 3 or 4):
    if(user_selection == 1):
      Addition(get_numbers())


start_calc()