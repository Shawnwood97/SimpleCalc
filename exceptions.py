class CalculatorInputError(ValueError):
  def __init__(self):
    super().__init__('You must enter a number! (int or float)')